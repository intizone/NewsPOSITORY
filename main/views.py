from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import User


def index(request):
    context = {}
    return render(request, 'front/index.html', context)

def category(request):
    context = {}
    return render(request, 'front/category.html', context)

def allnews(request):
    context = {}
    return render(request, 'front/allnews.html', context)


def contact(request):
    context = {}
    return render(request, 'front/contact.html', context)



def dashboard(request):
    users = User.objects.all().count()
    news = models.Product.objects.filter(is_active=True).count()
    regions = models.Region.objects.all().count()
    category = models.Category.objects.all().count()

    context = {
        'users':users,
        'news':news,
        'regions':regions,
        'category':category
    }

    return render(request, 'dashboard/index.html', context)




def create_region(request):
    if request.method == 'POST':
        models.Region.objects.create(
            name=request.POST['name']
        )
        return redirect('regions')
    return render(request, 'dashboard/region/create.html')


def regions(request):
    regions = models.Region.objects.all()
    return render(request, 'dashboard/region/list.html', {'regions':regions})



def region_update(request, id):
    region = models.Region.objects.get(id=id)
    if request.method == 'POST':
        region.name = request.POST['name']
        region.save()
        return redirect('regions')
    return render(request, 'dashboard/region/update.html', {'region':region})


def region_delete(request, id):
    models.Region.objects.get(id=id).delete()
    return redirect('regions')







def category_delete(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('categorys')

def category_update(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('categorys')
    return render(request, 'dashboard/category/update.html', {'category':category})

def create_category(request):
    if request.method == 'POST':
        models.Category.objects.create(
            name=request.POST['name']
        )
        return redirect('categorys')
    return render(request, 'dashboard/category/create.html')

def categorys(request):
    categorys = models.Category.objects.all()
    return render(request, 'dashboard/category/list.html', {'categorys':categorys})