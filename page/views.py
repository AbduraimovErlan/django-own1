from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


menu = [{'title': "Все потоки", 'url_name': 'about_all'},
        {'title': "Разработка", 'url_name': 'development'},
        {'title': "Администрирование", 'url_name': 'administration'},
        {'title': "Дизайн", 'url_name': 'design'},
        {'title': "Менеджмент", 'url_name': 'management'},
        {'title': "Маркетинг", 'url_name': 'marketing'},
        {'title': "Научпоп", 'url_name': 'science'},
]

def index(request):
    posts = Posts.objects.all()
    cats = Category.objects.all()
    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': "Главная страница",
               'cat_selected': 0,
    }

    return render(request, 'index.html', context=context)
def about_all(request):
    return render(request, 'about_all.html', {'menu': menu, 'title': 'Все потоки'})

def development(request):
    return HttpResponse("Разработка")

def administration(request):
    return HttpResponse("Администрирование")

def design(request):
    return HttpResponse("Дизайн")

def management(request):
    return HttpResponse("Менеджмент")

def marketing(request):
    return HttpResponse("Маркетинг")

def science(request):
    return HttpResponse("Научпоп")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'post.html', context=context)

def show_category(request, cat_id):
    posts = Posts.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': "Отображение по рубрикам",
               'cat_selected': 0,
               }

    return render(request, 'index.html', context=context)


def detail(request, article_id):
    try:
        a = Posts.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдено!")

    latest_comment_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})


def leave_comment(request, article_id):
    try:
        a = Posts.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдено!")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))



