from news.models import News
from django.shortcuts import render




def news(request):
    news = News.objects.all().order_by("-id")

    return render(request, 'news.html', context = {"news":news})