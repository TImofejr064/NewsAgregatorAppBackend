from newsapi import NewsApiClient
from .models import *
import time

newsapi = NewsApiClient(api_key='990b728f8ea245bfbc63329adfd21522')


def eternalUpdatenewsLoop():
    __updateNews()
    time.sleep(3600)

def __updateNews():
    categories = Category.objects.all()
    News.objects.all().delete()
    for category in categories:
        print(category.category, ' ',category.category_for_api, ' ',category.image )
        if category.category_for_api == 'russia':
            news = __get_top_headlines(page_size=20, page=1)
            for article in news['articles']:
                n = News(headline=article['title'], description=article['description'], url_to_record=article['url'], url_to_image=article['urlToImage'], date=article['publishedAt'], category=category)
                n.save()
        else:
            news = __get_top_headlines(category=category.category_for_api, page_size=20, page=1)
            for article in news['articles']:
                n = News(headline=article['title'], description=article['description'], url_to_record=article['url'], url_to_image=article['urlToImage'], date=article['publishedAt'], category=category)
                n.save()


def __get_top_headlines( page, page_size=10,category=None):
    if category == None:
        top_headlines = newsapi.get_top_headlines(page_size=page_size, page=page, country='ru')
    else:
        top_headlines = newsapi.get_top_headlines(category=category, page_size=page_size, page=page, country='ru')

    if top_headlines['status'] == 'error':
        context = None
        return context
    elif top_headlines['status'] == 'ok':
        context = top_headlines
        return context