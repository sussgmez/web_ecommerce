# Generated by Django 4.0.2 on 2022-03-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_categoria_alter_product_imagen2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='precio_total',
            field=models.FloatField(default=0, editable=False, verbose_name='Precio Total'),
            preserve_default=False,
        ),
    ]