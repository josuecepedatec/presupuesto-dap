# Generated by Django 4.2.10 on 2024-05-16 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='pdf',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]