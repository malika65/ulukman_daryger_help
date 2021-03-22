from news.models import (
    Comments,
    ForumInfo,
    
)
from django.shortcuts import render,redirect
from news.forms import CommentsForm


def forum(request):
    info = ForumInfo.objects.all()
    comments = Comments.objects.all().order_by("-id")
    form = CommentsForm(request.POST)
    if request.method == "POST":
        save_form = CommentsForm(request.POST)
        if save_form.is_valid():
            comment = save_form.save()
           
            return redirect('news:forum')
    else:
        form = CommentsForm()
    
    return render(request, 'forum.html',{"form":form,"comments":comments,"info":info})