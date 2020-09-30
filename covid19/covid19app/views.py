from django.shortcuts import render
from urllib.request import urlopen
import requests
import json


def home(request):
    data = []
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Israel"}

    headers = {
      'x-rapidapi-host': "covid-193.p.rapidapi.com",
      'x-rapidapi-key': "9daf3970fbmsh1cdca461f3db3e5p1b1509jsn892176974102"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    d = response['response']
    s = d[0]

    context = {
        'all': s['cases']['total'],
        'recovered': s['cases']['recovered'],
        'deaths': s['deaths']['total'],
        'new': s['cases']['new'],
        'serioz': s['cases']['critical'],
        'tests' : s['tests']['total'],
        'ontime' : s['day'],

    }
    
   
    print(d)
    return render(request, 'home.html', context)


