# Generated by Django 4.2.16 on 2024-09-27 09:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0013_alter_comment_options_rename_postc_comment_post"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="post",
            new_name="postc",
        ),
    ]
