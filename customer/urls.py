from django.urls import path
from .views import CustomerUpdateView
urlpatterns=[
    path('<uuid:pk>/', CustomerUpdateView.as_view(), name='customer-detail'),
    path('<uuid:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('<uuid:pk>/delete/', CustomerUpdateView.as_view(), name='customer-delete'),
]