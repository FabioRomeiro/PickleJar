# Generated by Django 3.2 on 2021-05-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210524_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passcoord',
            field=models.BinaryField(default=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
