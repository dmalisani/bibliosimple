# Generated by Django 2.0.4 on 2018-04-23 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libros.Materia')),
            ],
        ),
        migrations.AlterField(
            model_name='libro',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libros.Submateria'),
        ),
    ]