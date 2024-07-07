from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
USER_TYPES = (
        ('Employee', 'employee'),
        ('Customer', 'customer')
    )
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=50,choices=USER_TYPES)
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

    
