# Generated by Django 3.1 on 2020-09-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApi', '0004_model_type_mod'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='ordre',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='model',
            name='window',
            field=models.IntegerField(default=72),
        ),
    ]
