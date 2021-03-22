from news.models import News,NewsImage
from django.shortcuts import render


def news_more(request,news_id):
    news = News.objects.get(id = news_id)
    image = news.images.all()
    image = NewsImage.objects.filter(news=news)

    
    return render(request, "new_more.html",{
        'news':news,
        'image': image
        })  
