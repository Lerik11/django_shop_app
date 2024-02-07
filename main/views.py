from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context  = {
        'content': 'Магазин мебели HOME',
        'title':'Home',
        }
    return render(request, 'main/index.html', context)

def about(request):
    context  = {
        'content': 'О нас',
        'title':'Home - О нас',
        'text_on_page' : 'Текст про наш крутой магазин'
        }
    return render(request, 'main/about.html', context=context)