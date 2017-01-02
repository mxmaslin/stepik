from django.http import HttpResponse
from django.shortcuts import render


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def login(request):
    return HttpResponse('login')


def signup(request):
    return HttpResponse('signup')


def question(request, some_pk):
    return HttpResponse('question')


def ask(request):
    return HttpResponse('ask')


def popular(request):
    return HttpResponse('popular')


def new(request):
    return HttpResponse('new')


def index(request):
    return HttpResponse('index')
