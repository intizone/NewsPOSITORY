from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'front/index.html', context)


def allnews(request):
    context = {}
    return render(request, 'front/allnews.html', context)

def category(request):
    context = {}
    return render(request, 'front/category.html', context)

def contact(request):
    context = {}
    return render(request, 'front/contact.html', context)