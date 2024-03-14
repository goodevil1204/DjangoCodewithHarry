from django.shortcuts import render
from django.http import HttpResponse
from . import models
def index(request):
    return render(request,"shop/index.html")

def about(request):
    return render(request,"shop/about.html")
<<<<<<< HEAD
=======
def about(request):
    return HttpResponse("About")
>>>>>>> aa03f9fd6ab6b719ea10fd1cdf9305ff623fe61b
def contact(request):
    return HttpResponse("contact")
def search(request):
    return HttpResponse("search")
def prodview(request):
    return HttpResponse("productview")
def tracker(request):
    return HttpResponse("tracker")
def Checkout(request):
    return HttpResponse("Checkout")
