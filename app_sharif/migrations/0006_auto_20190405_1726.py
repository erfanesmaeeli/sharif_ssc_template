# Generated by Django 2.1.7 on 2019-04-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sharif', '0005_grid_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='active',
            field=models.BooleanField(default='True'),
        ),
        migrations.AlterField(
            model_name='grid',
            name='description',
            field=models.TextField(null='True'),
        ),
        migrations.AlterField(
            model_name='grid',
            name='title',
            field=models.CharField(max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=100, null='True'),
        ),
    ]
