# Generated by Django 4.2.10 on 2024-05-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_factura_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='pdf',
            field=models.FileField(upload_to='pdfs'),
        ),
    ]
