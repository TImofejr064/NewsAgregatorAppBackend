# Generated by Django 3.0.9 on 2020-08-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200805_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='url_to_image',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка на фото'),
        ),
    ]
