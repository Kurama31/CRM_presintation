from django.shortcuts import render, redirect
from requests import auth

from django.contrib import auth

def blog(request):
    get_auth = auth.get_user(request).username
    #get_user_id = auth.get_user(request).id
    #print("request ------------->", auth.get_user(request).username)
    data = {
        'get_auth': get_auth
    }
    return render(request, 'blog/blog_index.html', data)