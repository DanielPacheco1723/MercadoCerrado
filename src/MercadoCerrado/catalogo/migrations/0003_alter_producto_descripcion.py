# Generated by Django 4.0.6 on 2022-08-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_alter_producto_descripcion_alter_producto_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
