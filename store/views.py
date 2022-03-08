from multiprocessing import context, get_context
from traceback import print_tb
from django.shortcuts import render, redirect
import unicodedata
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from .models import Producto, Pedido
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView):
    template_name = 'store/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos_destacados"] = Producto.objects.filter(destacado=True)[0:2]
        return context
    
    def post(self, request, **kwargs):
        user = autenticar_usuario(request)
        ctx = self.get_context_data(**kwargs)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.get_full_path())
        ctx.update({'error_login':True, 'nohide':'no-hide'})
        return render(request, self.template_name, ctx)

class SearchView(TemplateView):
    template_name = 'store/search.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        min_precio = 0
        max_precio = 0
        try:
            min_precio = float(self.request.GET['min'])
        except: pass

        try:
            max_precio = float(self.request.GET['max'])
        except: pass

        productos_encontrados = self.search(self.request.GET['search'], min_precio, max_precio)
        
        #Menos de 10 | Entre 10 y 20 | Entre 20 y 50 | Entre 50 y 100 | Entre 100 y 200 | Entre 200 y 500 | Más de 500
        precios = [0,0,0,0,0,0,0]
        for producto in productos_encontrados:
            if producto.precio<=10: precios[0]+=1
            elif producto.precio>10 and producto.precio<=20: precios[1]+=1
            elif producto.precio>20 and producto.precio<=50: precios[2]+=1
            elif producto.precio>50 and producto.precio<=100: precios[3]+=1
            elif producto.precio>100 and producto.precio<=200: precios[4]+=1
            elif producto.precio>200 and producto.precio<=500: precios[5]+=1
            elif producto.precio>500: precios[6]+=1
                   
        context['precios'] = precios
        context['productos'] = productos_encontrados

        return context

    def search(self, k_search, min_precio, max_precio):
        productos = Producto.objects.all()
        productos_encontrados = []
        k_search = self.limpiar_cadena(k_search).lower()
        for producto in productos:
            if producto.categoria == None: producto.categoria = ""
            if self.limpiar_cadena(producto.nombre).lower().count(k_search)>=1 or self.limpiar_cadena(producto.categoria).lower().count(k_search)>=1:
                if min_precio!=0 and max_precio==0:
                    if producto.precio>min_precio:
                        productos_encontrados.append(producto)
                elif min_precio==0 and max_precio!=0:
                    if producto.precio<=max_precio:
                        productos_encontrados.append(producto)
                elif min_precio!=0 and max_precio!=0:
                    if producto.precio>min_precio and producto.precio<=max_precio:
                        productos_encontrados.append(producto)
                else:
                    productos_encontrados.append(producto)
        return productos_encontrados

    def limpiar_cadena(self, cadena):
        return unicodedata.normalize('NFKD', cadena).encode('ASCII', 'ignore').decode('ASCII')

    def post(self, request, **kwargs):
        user = autenticar_usuario(request)
        ctx = self.get_context_data(**kwargs)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.get_full_path())
        ctx.update({'error_login':True, 'nohide':'no-hide'})
        return render(request, self.template_name, ctx)

class ProductView(TemplateView):
    template_name = 'store/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producto'] = Producto.objects.get(pk=kwargs['id'])
        context['productos_relacionados'] = Producto.objects.filter(categoria=context['producto'].categoria)
        context['productos_relacionados'] = context['productos_relacionados'].exclude(pk=kwargs['id'])
        if self.request.GET.__len__() > 0:
            if self.request.user.is_anonymous:
                context['nohide'] = 'no-hide'
        return context

    def get(self, request, *args, **kwargs):
        if self.request.GET.__len__() > 0:
            if not self.request.user.is_anonymous:
                producto = Producto.objects.get(pk=self.request.GET['product_id'])
                cantidad = int(self.request.GET['cantidad'])
                Pedido.objects.create(user=self.request.user, producto=producto, cantidad=cantidad, precio_total=producto.precio*cantidad)
                return HttpResponseRedirect('/orders/')
        return super().get(request, *args, **kwargs)

    def post(self, request, **kwargs):
        user = autenticar_usuario(request)
        ctx = self.get_context_data(**kwargs)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.get_full_path())
        ctx.update({'error_login':True, 'nohide':'no-hide'})
        return render(request, self.template_name, ctx)
    
class OrdersView(LoginRequiredMixin, TemplateView):
    template_name = 'store/orders.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedidos'] = Pedido.objects.filter(user=self.request.user).order_by('-updated')
        return context
    
def delete_order(request, id):
    Pedido.objects.filter(pk=id).delete()
    return HttpResponseRedirect('../orders/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('../home/')

def redirect(request):
    return HttpResponseRedirect('../home/')

def autenticar_usuario(request):
    datos = request.POST
    username = datos['username'] 
    password = datos['password']
    user = authenticate(request, username=username, password=password)
    return user