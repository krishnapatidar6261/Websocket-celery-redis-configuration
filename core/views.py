from django.shortcuts import render
from django.http import HttpResponse,response
from .tasks import *
# Create your views here.


def index(request):
    return HttpResponse({"status":True})


def check_celery_working(request,name="krishna"):

    run_task.delay(name)
    return HttpResponse("working")