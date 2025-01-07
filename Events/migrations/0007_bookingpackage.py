# Generated by Django 5.1.4 on 2024-12-23 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_alter_weddingpackage_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=254)),
                ('mobile_no', models.IntegerField()),
                ('additional_services', models.TextField(blank=True, help_text='Enter additional service requests.')),
                ('booking_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('weddingpackage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weddingpackage', to='Events.weddingpackage')),
            ],
        ),
    ]
