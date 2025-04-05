# Generated by Django 5.2 on 2025-04-05 06:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_mission_image_vision_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(max_length=200, upload_to='images/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
