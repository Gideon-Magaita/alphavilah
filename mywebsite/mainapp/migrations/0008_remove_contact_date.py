# Generated by Django 5.2 on 2025-04-05 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_contact_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]
