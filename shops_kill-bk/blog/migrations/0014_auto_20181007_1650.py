# Generated by Django 2.1.1 on 2018-10-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20181007_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_users',
            name='addtime',
            field=models.DateTimeField(null=True, verbose_name='发布时间'),
        ),
    ]
