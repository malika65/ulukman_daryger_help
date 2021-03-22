from news.models import People

from django.shortcuts import render




def himaya_ch(request):
    child = People.objects.filter(gender='3').order_by("-id")
    return render(request, 'himaya_ch.html', context = {"child":child})