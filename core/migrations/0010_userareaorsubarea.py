# Generated by Django 4.2.10 on 2024-05-24 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_factura_cesta_factura_folio_de_entrada_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAreaOrSubArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.area')),
                ('sub_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subarea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
