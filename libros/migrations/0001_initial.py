# Generated by Django 2.0.4 on 2018-04-23 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Editoriales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('anno', models.CharField(blank=True, help_text='Año de edición', max_length=4, null=True, verbose_name='año')),
                ('edicion', models.CharField(blank=True, help_text='Versión de edición', max_length=13, null=True, verbose_name='Edición')),
                ('isbn', models.CharField(max_length=200)),
                ('autor', models.CharField(help_text='Autor o autores (separados por , )', max_length=250)),
                ('codigo', models.CharField(blank=True, max_length=14, null=True)),
                ('estado', models.CharField(blank=True, choices=[('N', 'Nuevo'), ('U', 'Uso normal'), ('D', 'Deteriorado'), ('I', 'Inulitilzable')], default='U', max_length=1, null=True)),
                ('nro_ejemplar', models.PositiveSmallIntegerField(default=1)),
                ('baja', models.BooleanField(default=False)),
                ('lengua_extranjera', models.BooleanField(default=False, help_text='Escrito en otro idioma (sin traducir)', verbose_name='Lengua extranjera')),
                ('claves', models.TextField(blank=True, help_text='ciertas palabras que permitan encontrar el ejemplar', null=True, verbose_name='Claves de búsqueda')),
                ('paginas', models.CharField(blank=True, max_length=14, null=True, verbose_name='Páginas')),
                ('formato', models.CharField(blank=True, help_text='Alto y ancho en cm', max_length=14, null=True, verbose_name='Formato')),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libros.Editorial')),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='libro',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libros.Materia'),
        ),
    ]