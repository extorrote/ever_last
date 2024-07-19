# Generated by Django 5.0.2 on 2024-07-06 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everapp', '0029_bar_recommendation_google_maps_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]