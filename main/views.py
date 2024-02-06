from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context  = {
        'title' : 'home', 
        'content' : 'Main page of this project is Home',
        'names' : ['Masha', 'Lera'],
        'age' : {'Masha': 22, 'Lera': 20},
        'is_auth': True
        }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')