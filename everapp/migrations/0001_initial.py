# Generated by Django 5.0.2 on 2024-06-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
                ('property_size', models.CharField(blank=True, max_length=40, null=True)),
                ('bedrooms', models.CharField(blank=True, max_length=50, null=True)),
                ('bathrooms', models.CharField(blank=True, max_length=50, null=True)),
                ('property_type', models.CharField(blank=True, max_length=200, null=True)),
                ('property_status', models.CharField(blank=True, max_length=50, null=True)),
                ('mls', models.CharField(blank=True, max_length=50, null=True)),
                ('agent_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mls_status', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('development_name', models.CharField(blank=True, max_length=50, null=True)),
                ('pre_construction', models.CharField(blank=True, max_length=50, null=True)),
                ('pet_friendly', models.CharField(blank=True, max_length=50, null=True)),
                ('primary_view', models.CharField(blank=True, max_length=50, null=True)),
                ('imagen1', models.ImageField(blank=True, null=True, upload_to='property')),
                ('imagen2', models.ImageField(blank=True, null=True, upload_to='property')),
                ('imagen3', models.ImageField(blank=True, null=True, upload_to='property')),
                ('imagen4', models.ImageField(blank=True, null=True, upload_to='property')),
                ('imagen5', models.ImageField(blank=True, null=True, upload_to='property')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'property',
                'verbose_name_plural': 'properties',
            },
        ),
    ]
