# Generated by Django 3.0.5 on 2020-05-08 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_name', models.CharField(max_length=258, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paginaweb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=258, unique=True)),
                ('url', models.URLField(unique=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeira_app.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeira_app.Paginaweb')),
            ],
        ),
    ]
