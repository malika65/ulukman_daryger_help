from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from news.urls import * 
from django.views.generic.base import RedirectView

urlpatterns = [
    path('selectlanguage/<str:user_language>', selectlanguage, name ='selectlanguage'),
    path('locale/<str:to_url>', locale, name ='locale'),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),


]

urlpatterns += i18n_patterns(
    path('', RedirectView.as_view(url='/ru/news/index/')),
    path('news/', include('news.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
