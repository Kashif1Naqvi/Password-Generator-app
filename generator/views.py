from django.shortcuts import render
from django.auth import HttpRequestResponce
# Create your views here.

def home(request):
  return HttpRequestResponce("Hello i am new i conding!")
