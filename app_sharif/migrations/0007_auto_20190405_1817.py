# Generated by Django 2.1.7 on 2019-04-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sharif', '0006_auto_20190405_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='grid',
            name='button',
            field=models.CharField(max_length=100, null='True'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='grid',
            name='description',
            field=models.TextField(default='', null='True'),
        ),
    ]
