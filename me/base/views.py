from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# creating first view
def tasklist(request):
    return HttpResponse('To Do list')

