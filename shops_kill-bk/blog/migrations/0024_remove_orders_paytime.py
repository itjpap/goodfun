# Generated by Django 2.1.1 on 2018-10-11 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='paytime',
        ),
    ]
