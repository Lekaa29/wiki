from django.shortcuts import render,redirect
from django import forms
import random
import subprocess
import json
import subprocess
from django.http import JsonResponse
from django.shortcuts import render

def scrape(request):
    # Start the scraper script in the background
    process = subprocess.Popen(['python', 'scrapeFOUND.py'])

    # Immediately return a response indicating that the scraper has started
    return JsonResponse({'status': 'Scraping started. Check back later for the result.'})

def index(request):
    #scrapeFOUND.scrape()
    return render(request, "encyclopedia/index.html")

