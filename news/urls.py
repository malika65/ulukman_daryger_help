from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'news'


urlpatterns = [
    path('index/', index,name="index"),
    path('news/', news,name="news_all"),
    path('social/', social, name="social"),
    path('himaya/', himaya,name="himaya"),
    path('himaya_men/', himaya_men,name="himaya_men"),
    path('himaya_ch/', himaya_ch,name="himaya_ch"),
    path('forum/', forum,name="forum"),
    path('newspaper/', newspaper,name='newspaper'),
    path('newspaper/pdf/<int:paper_id>/', open_pdf,name='pdf'),
    path('news/<int:news_id>/', news_more, name='news_more'),
    path('payment/<int:pay_id>',payment,name="payment"),
    path('payment_for_me', payment_for_me,name="payment_for_me"),
    path('gallery/', gallery,name='gallery'),
    path('team/', team, name="team"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
