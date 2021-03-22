from news.models import ShowPhoto
from django.shortcuts import render

def gallery(request):
    images = ShowPhoto.objects.all()
    return render(request, 'gallery.html', context={"images":images})
