from django.shortcuts import redirect
from django.http import HttpResponse,FileResponse,HttpResponseRedirect,JsonResponse

#  Language part 
def locale(request,to_url):
    full_url = str(request.META.get('HTTP_REFERER'))
    part_url = full_url.split('/')
    lang_code = part_url[3]
    file_url = part_url[4]
    language = lang_code
    return redirect("/"+language+"/"+file_url+"/"+to_url)