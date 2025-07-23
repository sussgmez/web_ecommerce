from django.db import models
from django.utils.translation import gettext_lazy as _ 
from simple_history.models import HistoricalRecords


class Category(models.Model):
    category = models.ForeignKey("ecommerce.Category", verbose_name=_("Categoría"), on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(_("Nombre"), max_length=100)


    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_("Nombre"), max_length=200)
    description = models.TextField(_("Descripción"))
    category = models.ForeignKey("ecommerce.Category", verbose_name=_("Categoría"), on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField(_("Precio"))
    history = HistoricalRecords()
    stock = models.IntegerField(_("Cantidad disponible"))


    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey("authentication.CustomUser", verbose_name=_("Usuario"), on_delete=models.CASCADE) 
    product = models.ForeignKey("ecommerce.Product", verbose_name=_("Producto"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Cantidad"))

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")


