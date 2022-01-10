from django.shortcuts import render
import requests



def Home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json() 
    articles = data['articles']

    context = {
        'articles' : articles
    }

    return render(request, 'home.html', context)
