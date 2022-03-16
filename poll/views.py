from django.shortcuts import render
from django.http import HttpResponse
# import datetime
# Create your views here.

def index(request):
    # now = datetime.datetime.now()
    # local = now.astimezone()
    return HttpResponse("Welcome to the Home page of the polling app")


def details(request, question_id):
    return HttpResponse("You're looking at question %s" %question_id)


def results(request, question_id):
    return HttpResponse("You're looking at results of  %s" %question_id)


def vote(request, question_id):
    return HttpResponse("You're looking at votes of question %s" %question_id)

