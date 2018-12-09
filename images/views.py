from django.shortcuts import render, render_to_response, redirect
import datetime as dt
from .models import Image, Location, Category
from django.http import HttpResponse, Http404

def default(request):
  pics = Image.all_images()
  print(pics)
  return render(request, 'all/pics.html', {'pics':pics})


