from django.urls import path
from .views import BillView,AnalyticsApiView
urlpatterns =[
  path("add/",BillView.as_view(),name="add"),
  # path("item/add/",BillItemView.as_view(),name="item-add"),
  path("",BillView.as_view(),name="total-bills"),
  path("analytics/",AnalyticsApiView.as_view(),name="analytics")
]