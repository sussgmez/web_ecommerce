from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("product/list/", views.ProductColorListView.as_view(), name="product-list"),
]
