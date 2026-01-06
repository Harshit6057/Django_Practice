from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  #return HttpResponse("Hello World! this is the home page")
  return render(request, 'index.html')

def about(request):
  return HttpResponse("About us page, this is about the page")

def contact(request):
  return HttpResponse("Contact us page, this is contact page")

