from news.models import People

from django.shortcuts import render,redirect
from django.urls import reverse
from news.forms import PaymentsInfoForm 
from google_currency import convert  
import json

def payment(request,pay_id):
    form = PaymentsInfoForm(request.POST)
    
    if request.method == "POST":
        women = People.objects.get(id = pay_id)
        money = int(request.POST['amount'])
        converted = convert('usd', 'kgs', money)
        json_acceptable_string = converted.replace("'", "\"")
        d = json.loads(json_acceptable_string)

        women.remaining_amount = str(float(women.money_for_collecting)- float(d['amount']))
        women.get_money = str(float(women.get_money) + float(d['amount']))
        women.save()
        save_form = PaymentsInfoForm(request.POST)

        if save_form.is_valid():
            women_w = save_form.save(commit=False)
            women_w.for_whom = women
            payment = save_form.save()
           
            return redirect('news:index')
    else:
        form = PaymentsInfoForm()
    return render(request,'payment.html',{"form":form})
