from django.shortcuts import render
from news.forms import PaymentsInfoForm


def payment_for_me(request):
    form = PaymentsInfoForm(request.POST)
    
    if request.method == "POST":
        save_form = PaymentsInfoForm(request.POST)
        if save_form.is_valid():
            payment = save_form.save()
           
            return redirect('news:index')
    else:
        form = PaymentsInfoForm()
    return render(request,'payment.html',{"form":form})