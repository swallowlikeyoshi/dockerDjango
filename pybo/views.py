from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def p1(request):
    return HttpResponse('장고를 이용한 url 매핑은 이렇게 하는 것입니다.')