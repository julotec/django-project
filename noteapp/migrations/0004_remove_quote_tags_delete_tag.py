# Generated by Django 5.0.2 on 2024-02-18 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0003_quote_user_tag_user_tag_tag_of_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]