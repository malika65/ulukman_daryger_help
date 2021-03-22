from news.models import People
from django.shortcuts import render

def himaya(request):
    women = People.objects.filter(gender='2').order_by("-id")
    return render(request, 'himaya_women.html', context = {"women":women})