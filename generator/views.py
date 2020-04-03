from django.shortcuts import render
import random
# Create your views here.

def home(request):
  return render(request,'generator/home.html')

def about(request):
  return render(request,'generator/about.html')

def password(request):
  character = list('abcdefghijklmnopqrstuvwxyz')
  if request.GET.get('uppercase'):
      character.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  if request.GET.get('specialchar'):
      character.extend('~!@#$%^&*()_+}{|":>?<>/')
  if request.GET.get('number'):
      character.extend('0123456789')
  length = int(request.GET.get('length'))
  thepassword = ''
  for i in range(length):
      thepassword += random.choice(character)
  return render(request,'generator/password.html',{'password':thepassword})