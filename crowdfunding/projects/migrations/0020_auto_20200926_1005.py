# Generated by Django 3.0.8 on 2020-09-26 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20200926_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='sup_expertise',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pledge',
            name='sup_exposure',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pledge',
            name='sup_facilities',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pledge',
            name='sup_resources',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
