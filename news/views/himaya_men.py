from news.models import People
from django.shortcuts import render

def himaya_men(request):
    men = People.objects.filter(gender='1').order_by("-id")
    return render(request, 'himaya_men.html', context = {"men":men})