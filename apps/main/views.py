from django.http import JsonResponse

from django.contrib import auth

from django.shortcuts import render, redirect

# https://www.youtube.com/watch?v=RKS81zzWWcM&t=1s

def main(request: render) -> JsonResponse:
    get_auth = auth.get_user(request).username

    data = {
        'get_auth': get_auth
    }
    #return render(request, 'news/news.html', data)
    return render(request, 'main/main_layout.html', data)

def about(request: render) -> JsonResponse:
    return render(request, 'main/about_us.html')


#def schedule(request):
#    template = loader.get_template('scheduler.html')
#    context = {}
#    rendered_page = template.render(context, request)
#    return HttpResponse(rendered_page)
