from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')
def contact(request):
    return render(request, 'mainapp/contact.html')
def developer(request):
    return render(request,'mainapp/developer.html')
def reservation(request):
    return render(request,'mainapp/reservation.html')
def about(request):
    return render(request,'mainapp/about.html')
def menu(request):
    return render(request,'mainapp/menu.html')
def blog(request):
    return render(request,'mainapp/blog.html')
