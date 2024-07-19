# Generated by Django 5.0.2 on 2024-06-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='google_maps',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='everapp'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='everapp'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='everapp'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='everapp'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imagen5',
            field=models.ImageField(blank=True, null=True, upload_to='everapp'),
        ),
    ]
