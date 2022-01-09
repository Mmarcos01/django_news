from django.shortcuts import render
import requests




def Home(request):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response = requests.get(url)
    # convert to json
    data = response.json() 
    print(data)
