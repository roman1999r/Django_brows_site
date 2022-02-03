# Generated by Django 3.0 on 2021-11-27 10:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211107_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='Url')),
                ('name', models.CharField(max_length=255)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='workphotos',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='Url'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=255, unique=True, verbose_name='Url')),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.DateTimeField()),
                ('name', models.TextField(max_length=255)),
                ('number', models.TextField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('instagram', models.CharField(max_length=255)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event', to='blog.Procedure')),
            ],
        ),
    ]
