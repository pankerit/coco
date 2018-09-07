# Generated by Django 2.1.1 on 2018-09-07 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('shoes_id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('shoes_type', models.CharField(blank=True, max_length=30, null=True)),
                ('color', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_before', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('image', models.FileField(upload_to='')),
                ('slug', models.CharField(max_length=200)),
            ],
        ),
    ]