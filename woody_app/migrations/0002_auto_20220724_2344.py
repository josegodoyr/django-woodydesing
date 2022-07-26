# Generated by Django 3.1.12 on 2022-07-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woody_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costo',
            name='detalle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='costo',
            name='tipo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='detalle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='lugar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='tipo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='detalle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='tipo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='cliente',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='estado',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='fecha_entrega',
            field=models.DateField(blank=True, null=True),
        ),
    ]