# Generated by Django 3.2.6 on 2021-08-09 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento_agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el Departamento', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito_agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el Distrito', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria_agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el Distrito', max_length=100)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 1')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 2')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 3')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 4')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Subir Imagen 5')),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia_turismo.distrito_agencia')),
            ],
        ),
        migrations.CreateModel(
            name='Recorrido_agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del Recorrido', max_length=150)),
                ('Recorrido1', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
                ('Recorrido2', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
                ('Recorrido3', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
                ('Recorrido4', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
                ('Recorrido5', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
                ('Recorrido6', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
                ('Recorrido7', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
                ('Recorrido8', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
                ('Recorrido9', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
                ('Recorrido10', models.CharField(blank=True, help_text='Primera Parada', max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios_agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el Distrito', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese su Nombre:', max_length=100)),
                ('apellido', models.CharField(help_text='Ingrese su Apellido:', max_length=100)),
                ('celular', models.IntegerField(help_text='Ingrese su Numero de Celular', max_length=9)),
                ('correo', models.EmailField(help_text='Ingrese su Correo Electronico', max_length=100)),
                ('ciudad', models.CharField(help_text='Ingrese su ciudad', max_length=100)),
                ('mensaje', models.CharField(help_text='Ingrese Un texto', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia_agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese la Provincia', max_length=100)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia_turismo.departamento_agencia')),
            ],
        ),
        migrations.CreateModel(
            name='Paquete_turistico_agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el Distrito', max_length=100)),
                ('slug_paquete', models.SlugField(blank=True, null=True)),
                ('hora_salida', models.TimeField()),
                ('hora_entrada', models.TimeField()),
                ('precio', models.FloatField(help_text='Ingrese el precio en Soles', max_length=100)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia_turismo.distrito_agencia')),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia_turismo.galeria_agencia')),
                ('recorrido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia_turismo.recorrido_agencia')),
                ('servicio', models.ManyToManyField(to='agencia_turismo.Servicios_agencia')),
            ],
        ),
        migrations.CreateModel(
            name='Evento_agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del Evento Turistico', max_length=250)),
                ('fecha', models.DateField()),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia_turismo.distrito_agencia')),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia_turismo.galeria_agencia')),
            ],
        ),
        migrations.AddField(
            model_name='distrito_agencia',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia_turismo.provincia_agencia'),
        ),
    ]