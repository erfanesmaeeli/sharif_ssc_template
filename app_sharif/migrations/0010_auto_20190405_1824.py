# Generated by Django 2.1.7 on 2019-04-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sharif', '0009_auto_20190405_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grid',
            name='button',
            field=models.CharField(default='اطلاعات بیشتر ', max_length=100),
        ),
    ]