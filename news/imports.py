from .models import (
    News,
    Newspaper,
    NewsImage, 
    People,
    Comments,
    ForumInfo,
    Gallery,
    ShowPhoto,
    Appeal
)

from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse,HttpResponseRedirect,JsonResponse
from django.utils.translation import get_language,activate,LANGUAGE_SESSION_KEY
from django.urls import reverse
import stripe
from django.utils import translation
from .forms import CommentsForm,PaymentsInfoForm,SendEmailForm
from django.contrib import messages
from google_currency import convert  
import json
from django.core.mail import send_mail
from django.conf import settings
from .utils import send_to_email