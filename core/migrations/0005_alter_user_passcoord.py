# Generated by Django 3.2 on 2021-05-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210524_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passcoord',
            field=models.BinaryField(),
        ),
    ]
