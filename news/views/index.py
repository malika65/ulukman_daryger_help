from news.models import News
from django.shortcuts import render, redirect
from news.forms import SendEmailForm
from news.utils import send_to_email

#  Main page index.html
def index(request):
    news = News.objects.all().order_by("-id")
    if request.method == "POST":
        save_form = SendEmailForm(request.POST)
        if save_form.is_valid():
            save_form.save()
            send_to_email((save_form.cleaned_data['theme']+' from : '+save_form.cleaned_data['name']+' \nEmail :'+save_form.cleaned_data['email']+'\n'+save_form.cleaned_data['comment']),settings.EMAIL_FROM)
            return redirect("news:index")
    else:
        form = SendEmailForm()

    return render(request, 'index_main.html', context = {"news":news,"form":form})
