import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
import mptt

# https://www.youtube.com/watch?v=RKS81zzWWcM&t=1s

#DRF connect to 1s
#https://github.com/ilyachch/django-rest-framework-rusdoc/blob/master/api-guide/authentication.md

def main(request: render) -> JsonResponse:


    data = {
        'title': 'Главная страница from Views',
        'values': ['Some', 'hello', '123'],
        'obj': {
            'car': 'BNW',
            'age': 18,
            'hobo': 'hobo'
        }
    }
    return render(request, 'main/main_layout.html', data)


def about(request: render) -> JsonResponse:




    return render(request, 'main/about_us.html')


#def schedule(request):
#    template = loader.get_template('scheduler_old.html')
#    context = {}
#    rendered_page = template.render(context, request)
#    return HttpResponse(rendered_page)
