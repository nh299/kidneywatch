from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def indexPageView(request):
    return render(request, 'index.html')

def infoPageView(request):
    return render(request, 'info.html')

def dashboardPageView(request):
    return render(request, 'dashboard.html')

def testPageView(request):
    return render(request, 'test.html')