# Generated by Django 3.0.9 on 2020-08-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_category_category_for_api'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_for_api',
            field=models.CharField(max_length=255, verbose_name='Категория для API'),
        ),
    ]