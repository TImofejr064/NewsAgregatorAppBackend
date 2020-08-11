from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name="Категория")
    category_for_api = models.CharField(max_length=255, verbose_name="Категория для API")
    image = models.CharField(max_length=255, verbose_name="Ссылка на фото")

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'Категория {self.category}'


class News(models.Model):
    headline = models.TextField(verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    url_to_record = models.CharField(max_length=255, verbose_name="Ссылка на ориг. запись")
    url_to_image = models.CharField(max_length=255, verbose_name="Ссылка на фото", blank=True)
    date = models.CharField(max_length=255, verbose_name="Дата")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Новости"

    def __str__(self):
        return {self.headline}