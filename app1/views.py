from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sushma(request):
    return HttpResponse('<h1><marquee>The future belongs to those who believe in the beauty of thier dreams</marquee></h1>')

