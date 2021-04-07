from news.models import Enterpreneurship,EnterpreneImage

from django.shortcuts import render


def social(request):
    enterpre = Enterpreneurship.objects.all()    
    return render(request, "social.html", context={"enterpre":enterpre})  