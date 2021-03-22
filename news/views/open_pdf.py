from news.models import Newspaper

from django.shortcuts import render,redirect
from django.http import FileResponse



def open_pdf(request,paper_id):
    news = Newspaper.objects.get(id=paper_id)
    n = news.pdf
    if request.method == 'GET':
        return FileResponse(open(f'media/{n}', 'rb'), content_type='application/pdf')
   