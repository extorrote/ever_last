# Generated by Django 5.0.2 on 2024-06-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everapp', '0020_alter_tour_recommendation_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_name', models.CharField(blank=True, max_length=200, null=True)),
                ('kind_of_art', models.CharField(blank=True, max_length=200, null=True)),
                ('range_of_price', models.CharField(blank=True, max_length=100, null=True)),
                ('title_h1', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=6000, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('days_open', models.CharField(blank=True, max_length=300, null=True)),
                ('open_hours', models.CharField(blank=True, max_length=300, null=True)),
                ('imagen1', models.ImageField(blank=True, null=True, upload_to='everapp')),
                ('imagen2', models.ImageField(blank=True, null=True, upload_to='everapp')),
                ('imagen3', models.ImageField(blank=True, null=True, upload_to='everapp')),
                ('imagen4', models.ImageField(blank=True, null=True, upload_to='everapp')),
            ],
            options={
                'verbose_name': 'recommend Gallery',
                'verbose_name_plural': 'recommend Galleries',
            },
        ),
        migrations.AlterModelOptions(
            name='recommendation',
            options={'verbose_name': ' Review ', 'verbose_name_plural': 'Reviews'},
        ),
    ]