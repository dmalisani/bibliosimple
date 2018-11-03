# Generated by Django 2.0.4 on 2018-04-23 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20180423_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submateria',
            options={'ordering': ['materia__nombre', 'nombre']},
        ),
        migrations.RemoveField(
            model_name='libro',
            name='materia',
        ),
        migrations.AddField(
            model_name='libro',
            name='submateria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='libros.Submateria', verbose_name='Materia'),
            preserve_default=False,
        ),
    ]