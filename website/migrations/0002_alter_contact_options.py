# Generated by Django 4.2.15 on 2024-09-20 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('createdDate',)},
        ),
    ]
