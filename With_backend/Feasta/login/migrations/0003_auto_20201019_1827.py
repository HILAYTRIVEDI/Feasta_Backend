# Generated by Django 3.1 on 2020-10-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20201019_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='Name',
            new_name='Product_name',
        ),
        migrations.AddField(
            model_name='user_info',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user_info',
            name='quantity',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='price',
            field=models.IntegerField(default='0.0'),
        ),
    ]
