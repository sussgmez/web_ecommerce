from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import ProductColor, Order, ProductSize
from .forms import OrderForm


class HomeView(TemplateView):
    template_name = "ecommerce/home.html"


class ProductColorListView(ListView):
    model = ProductColor
    template_name = "ecommerce/_product_list.html"
    

class ProductColorDetailView(DetailView):
    model = ProductColor
    template_name = "ecommerce/_product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["colors"] = ProductColor.objects.filter(product__pk=self.get_object().product.pk)
        return context
    

class OrderCreateView(CreateView):
    model = Order
    template_name = "ecommerce/_order_create.html"
    form_class = OrderForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = ProductSize.objects.get(pk=self.request.GET['size'])
        context["max_quantity"] = range(1, context["product"].stock + 1) if context["product"].stock < 10 else range(1, 11) 
        return context
    
    
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("product", ProductSize.objects.get(pk=request.POST['product']).product_color.pk)
            
        return super().post(request, *args, **kwargs)
