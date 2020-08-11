# Generated by Django 3.0.9 on 2020-08-04 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200804_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.CharField(max_length=155, verbose_name='Ссылка на фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category', verbose_name='Категория'),
        ),
    ]