# Generated by Django 4.2.10 on 2024-05-21 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_area_proveedor_subarea_tipodegasto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='en_linea',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='aula_virtual',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='live',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='posgrados_en_linea',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='posgrados_presencial',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='s1_0700399A03',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='s1_0700399A31',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='s1_0705103A00',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='s1_0870399A06',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='s1_0875103A00',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='the_learning_gate',
            field=models.IntegerField(default=0),
        ),
    ]
