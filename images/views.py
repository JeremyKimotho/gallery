from django.shortcuts import render, render_to_response, redirect
import datetime as dt
from .models import Image
from django.http import HttpResponse, Http404

def welcome(request):
  return render(request, 'welcome.html')
