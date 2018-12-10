from django.shortcuts import render, render_to_response, redirect
import datetime as dt
from .models import Image, Location, Category
from django.http import HttpResponse, Http404

def default(request):
  pics = Image.all_images()
  return render(request, 'all/pics.html', {'pics':pics})

def filter_usa(request):
  pics = Image.filter_images('USA')
  return render(request, 'all/search.html', {'pics':pics})

def filter_germany(request):
  pics = Image.filter_images('Germany')
  return render(request, 'all/search.html', {'pics':pics})

def filter_italy(request):
  pics = Image.filter_images('Italy')
  return render(request, 'all/search.html', {'pics':pics})

def filter_brazil(request):
  pics = Image.filter_images('Brazil')
  return render(request, 'all/search.html', {'pics':pics})

def filter_kenya(request):
  pics = Image.filter_images('Kenya')
  return render(request, 'all/search.html', {'pics':pics})

def search(request):
  if 'location' in request.GET and request.GET['location']:
    search_term = request.GET.get('location')
    searched_pics = Image.search_image(search_term)
    return render(request, 'all/search.html', {'pics':searched_pics})

  else:
    return render(request, 'all/search.html')
