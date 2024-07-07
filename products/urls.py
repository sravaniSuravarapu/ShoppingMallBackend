from django.urls import path
from .views import ProductView,ProductDetailView
urlpatterns =[
    path("",ProductView.as_view(),name="product-list"),
    path('add/',ProductView.as_view(),name="add"),
    path("<int:pk>/",ProductDetailView.as_view(),name="product-detail"),
    path("<int:pk>/update",ProductDetailView.as_view(),name="product-detail-update"),
    path("<int:pk>/delete",ProductDetailView.as_view(),name="product-detail-delete"),
]