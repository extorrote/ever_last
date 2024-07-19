# Generated by Django 5.0.2 on 2024-06-20 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everapp', '0007_rename_date_time_appointment_appointment_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('recommendation', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]