# Generated by Django 2.1.1 on 2018-10-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20181007_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_users',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='发布时间'),
        ),
    ]
