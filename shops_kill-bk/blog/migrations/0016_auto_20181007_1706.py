# Generated by Django 2.1.1 on 2018-10-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20181007_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_users',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='注册时间'),
        ),
        migrations.AlterField(
            model_name='shop_users',
            name='headerimg',
            field=models.ImageField(null=True, upload_to='', verbose_name='头像'),
        ),
    ]
