from django.shortcuts import render
import requests



def Home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json() 
    articles = data['articles']
    
    context = {
        'articles' : articles
    }

    return render(request, 'home.html', context)
