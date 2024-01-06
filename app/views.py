from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
# Create your views here.
def topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=="POST":
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid:
            TFDO.save()
            return HttpResponse("Topic created successfully")
        else:
            return HttpResponse("invalid data")
    return render(request,'topic.html',d)

def webpage(request):
    EWFO=WebPageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebPageForm(request.POST)
        if WFDO.is_valid:
            WFDO.save()
            return HttpResponse("webpages created successfully")
        else:
            return HttpResponse("Invalide Data")
    return render(request,'webpage.html',d)

def accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid:
            AFDO.save()
            return HttpResponse("access recode  created successfully")
        else:
            return HttpResponse("Invalide Data")
    return render(request,'accessrecord.html',d)