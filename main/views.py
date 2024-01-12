# from django.shortcuts import render 
# from django.http import HttpResponse
# # from .models import 

# def index(request):
#     return render(request, 'index.html')


from django.shortcuts import render 
from django.http import HttpResponse
# from .models import Food, Reservation, Post, Sign

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

# def index(request):
#     return render (request, 'index.html')

def categori(request):
    return render(request, 'categori.html')

def contact(request):
    return render (request, 'contact.html')

def latest_news(request):
    return render (request, 'latest_news.html')