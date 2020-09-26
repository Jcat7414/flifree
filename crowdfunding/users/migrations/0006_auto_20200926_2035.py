# Generated by Django 3.0.8 on 2020-09-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200914_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='admin',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='admin'),
        ),
    ]
