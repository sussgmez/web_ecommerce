from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=256)
    
    imagen = models.ImageField(verbose_name='Imagen', upload_to='products/')
    imagen2 = models.ImageField(verbose_name='Imagen 2', upload_to='products/', blank=True, null=True)
    imagen3 = models.ImageField(verbose_name='Imagen 3', upload_to='products/', blank=True, null=True)
    imagen4 = models.ImageField(verbose_name='Imagen 4', upload_to='products/', blank=True, null=True)
    
    precio = models.FloatField(verbose_name='Precio', blank=True, null=True)
    
    num_disponibles = models.BigIntegerField(verbose_name='Disponibles', blank=True, null=True)
    
    categoria = models.CharField(verbose_name='Categoria', max_length=100, blank=True, null=True)
    marca = models.CharField(verbose_name='Marca', max_length=100, blank=True, null=True)
    
    destacado = models.BooleanField(verbose_name='Destacado', default=False)
    
    created = models.DateTimeField(verbose_name='Creado el', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última actualización', auto_now=True)

    def __str__(self) -> str:
        return "{} | Disponibles: {}".format(self.nombre, self.num_disponibles)

class Pedido(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio_total = models.FloatField(verbose_name='Precio Total')

    created = models.DateTimeField(verbose_name='Creado el', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Última actualización', auto_now=True)

    def __str__(self) -> str:
        return "{}: {} * {} | {}".format(self.id, self.producto.nombre, self.cantidad, self.user)

@receiver(pre_save, sender=Pedido)
def ajustar_inventario(sender, instance, *args, **kwargs):
    mismo_producto = True

    try:
        if (sender.objects.get(id=instance.id).producto != instance.producto):
            mismo_producto = False
    except: pass

    if mismo_producto:
        cantidad_anterior = 0
        try:
            cantidad_anterior = sender.objects.get(id=instance.id).cantidad
        except: pass
        diferencia_cantidad = cantidad_anterior - instance.cantidad
        instance.producto.num_disponibles += diferencia_cantidad
        
        if instance.producto.num_disponibles < 0:
            raise Exception('Cantidad no disponible')
        else:
            instance.producto.save()

    else:
        pedido_viejo = sender.objects.get(id=instance.id)
        pedido_viejo.producto.num_disponibles += pedido_viejo.cantidad
        pedido_viejo.producto.save()

        instance.producto.num_disponibles -= instance.cantidad
        if instance.producto.num_disponibles < 0:
            raise Exception('Cantidad no disponible')
        else:
            instance.producto.save()

@receiver(pre_save, sender=Pedido)
def set_precio_total(sender, instance, *args, **kwargs):
    instance.precio_total = instance.cantidad * instance.producto.precio

@receiver(post_save, sender=Pedido)
def borrar_si_0(sender, instance, **kwargs):
    if instance.cantidad == 0:
        instance.delete()

@receiver(post_delete, sender=Pedido)
def ajustar_inventario_2(sender, instance, **kwargs):
    instance.producto.num_disponibles += instance.cantidad
    instance.producto.save()