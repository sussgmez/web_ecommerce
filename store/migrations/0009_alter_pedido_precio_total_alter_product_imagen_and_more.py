# Generated by Django 4.0.2 on 2022-03-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_pedido_updated_alter_product_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='precio_total',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio Total'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(upload_to='products/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen 3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen 4'),
        ),
    ]