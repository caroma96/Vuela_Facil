# Generated by Django 3.2.7 on 2021-10-05 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vuelos', '0001_initial'),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('dcto', models.FloatField(default=0)),
                ('pagado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Usuarios.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Tiquete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('tipoSilla', models.CharField(max_length=50)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkout.carritocompras')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Vuelos.tipovuelo')),
            ],
        ),
    ]
