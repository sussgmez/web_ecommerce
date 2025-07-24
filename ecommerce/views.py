from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import ProductColor


class HomeView(TemplateView):
    template_name = "ecommerce/home.html"


class ProductColorListView(ListView):
    model = ProductColor
    template_name = "ecommerce/_product_list.html"


