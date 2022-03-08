# Generated by Django 4.0.2 on 2022-03-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_pedido_created_pedido_updated_product_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Última actualización'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(upload_to='products/<django.db.models.fields.CharField>', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='products/<django.db.models.fields.CharField>', verbose_name='Imagen 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='products/<django.db.models.fields.CharField>', verbose_name='Imagen 3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='products/<django.db.models.fields.CharField>', verbose_name='Imagen 4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Última actualización'),
        ),
    ]