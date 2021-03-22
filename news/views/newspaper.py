from news.models import Newspaper

from django.shortcuts import render

def newspaper(request):
    newspapers = Newspaper.objects.all().order_by("-id")
    return render(request, 'newspaper.html', context={"newspaper":newspapers})
