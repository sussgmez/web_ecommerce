from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("product/list/", views.ProductColorListView.as_view(), name="product-list"),
    path("product/<int:pk>/", views.ProductColorDetailView.as_view(), name="product"),
    path("order/create/", views.OrderCreateView.as_view(), name="order-create"),
]
