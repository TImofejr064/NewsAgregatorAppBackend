# Generated by Django 3.0.9 on 2020-08-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200804_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_for_api',
            field=models.CharField(default='asd', max_length=255, verbose_name='Категория для API'),
        ),
    ]
