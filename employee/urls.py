from django.urls import path
from .views import EmployeeDetailView
urlpatterns =[
  path("<uuid:pk>/",EmployeeDetailView.as_view(),name="employee-retrive"),
  path("<uuid:pk>/update/",EmployeeDetailView.as_view(),name="employee-update"),
  path("<uuid:pk>/delete/",EmployeeDetailView.as_view(),name="employee-delete"),
]