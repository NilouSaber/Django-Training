# Generated by Django 4.2.16 on 2024-09-22 17:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_alter_contact_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="family",
        ),
    ]
