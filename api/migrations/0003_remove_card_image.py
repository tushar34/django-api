# Generated by Django 3.2.5 on 2021-07-27 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_card_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='image',
        ),
    ]