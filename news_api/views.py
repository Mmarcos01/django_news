from django.shortcuts import render
import requests

# move to env
API_KEY = '141063e5e50941c9a61678a0beacfc78'


def Home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    # if country:
    #     url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    #     response = requests.get(url)
    #     data = response.json() 
    #     articles = data['articles']
    # else:
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json() 
    articles = data['articles']

    context = {
        'articles' : articles
    }

    return render(request, 'home.html', context)
