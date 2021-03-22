from django.http import HttpResponseRedirect
from django.utils.translation import activate,LANGUAGE_SESSION_KEY
from django.utils import translation


def selectlanguage(request, user_language):
    a = str(request.META.get('HTTP_REFERER'))
    b = a.split('/')
    c = b[4:]
    c = '/'.join(c)
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY]=user_language
    return HttpResponseRedirect("/"+user_language+"/"+c)