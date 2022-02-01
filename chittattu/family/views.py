from django.http import HttpResponse
from django.shortcuts import render

def display1(request):
    return HttpResponse('welcome to my family')


