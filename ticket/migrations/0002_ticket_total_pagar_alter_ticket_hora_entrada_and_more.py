# Generated by Django 4.1.1 on 2022-10-06 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_remove_vehiculo_hora_entrada_and_more'),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='total_pagar',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hora_entrada',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='idVehiculo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculo.vehiculo'),
        ),
    ]
