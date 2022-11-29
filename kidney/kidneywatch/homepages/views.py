from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.

def indexPageView(request):
    return render(request, 'index.html')

def infoPageView(request):
    return render(request, 'info.html')

def dashboardPageView(request):
    return render(request, 'dashboard.html')

def testPageView(request):
    return render(request, 'test.html')

def dataRender(request):
    search = request.POST.get('searchFood')
    parameters = { 
        "api_key": 'EPMl3IkB2Wb9GzdAbcfaaYkCCucSG7JQxbGUoWGK',
        "query": search,
        "dataType": ["Foundation"]
    }
    if search != None:
        response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params=parameters)

        data = response.json()
        foods=[]
        for f in range(len(data['foods'])):
            food = data["foods"][f]['description']
            foods.append(food)
        context = {
            'foods':foods
        }
        return render(request, 'test.html', context)
    else:
        return render(request, 'test.html')
