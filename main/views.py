from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import User

def create_product(request):

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category = models.Category.objects.get(id=request.POST['category_id'])
        region = models.Region.objects.get(id=request.POST['region_id'])
        image = request.FILES['image']
        
        models.product.objects.create(
            name=name,
            description = description,
            category = category,
            region = region,
            image=image
        )
        return redirect('products')
    context = {
        'categorys':models.Category.objects.all(),
        'regions':models.Region.objects.all()
    }
    return render(request, 'dashboard/product/create.html', context)


def products(request):
    products = models.Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'dashboard/product/list.html', context)


def product_update(request, id):
    product = models.Product.objects.get(id=id)
    if request.method == 'POST':
        category = models.Category.objects.get(id=request.POST['category_id'])
        region = models.Region.objects.get(id=request.POST['region_id'])
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.category=category
        product.region=region
        image = request.FILES.get('image')
        if image:
            product.image = image
        product.save()

    context = {
        'product':product,
        'categorys':models.Category.objects.all(),
        'regions':models.Region.objects.all()
    }
    return render(request, 'dashboard/product/update.html', context)


def product_delete(request, id):
    models.product.objects.get(id=id).delete()
    return redirect('products')



# def products(request):

#     category_id = request.GET.get('category_id')
#     categorys = models.Category.objects.all().order_by('name')

#     if category_id:
#         category = models.Category.objects.get(id=category_id)
#         product = models.product.objects.filter(category=category, is_active=True)
#         status = category
#     else:
#         status = 0
#         product = models.product.objects.filter(is_active=True)

#     context = {
#         'product':product,
#         'categorys':categorys,
#         'status':status
#     }
#     return render(request, 'front/product.html', context)







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
    allnews = models.Product.objects.filter(is_active=True).count()
    regions = models.Region.objects.all().count()
    categorys = models.Category.objects.all().count()

    context = {
        'users':users,
        'allnews':allnews,
        'regions':regions,
        'categorys':categorys
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

# def products(request):
#     products = models.Product.objects.all()
#     return render(request, 'dashboard/product/list.html', {'products':products})

def product_delete(request, id):
    models.Product.objects.get(id=id).delete()
    return redirect('products')

def product_update(request, id):
    product = models.Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.category = models.Category.objects.get(id=request.POST['category'])
        product.region = models.Region.objects.get(id=request.POST['region'])
        product.save()
        return redirect('products')
    return render(request, 'dashboard/product/update.html', {'product':product})

def create_product(request):
    if request.method == 'POST':
        models.Product.objects.create(
            name = request.POST['name'],
            category=models.Category.objects.get(id=request.POST['category']),
            region=models.Region.objects.get(id=request.POST['region'])
        )
        return redirect('products')
    return render(request, 'dashboard/product/create.html')



def forms(request):
    forms = models.Form.objects.all()
    return render(request, 'dashboard/form/list.html', {'forms':forms})

def form_delete(request, id):
    models.Form.objects.get(id=id).delete()
    return redirect('forms')

def form_update(request, id):
    form = models.Form.objects.get(id=id)
    if request.method == 'POST':
        form.name = request.POST['name']
        form.email = request.POST['email']
        form.body = request.POST['body']
        form.is_checked = request.POST.get('is_checked', False)
        form.save()
        return redirect('forms')
    return render(request, 'dashboard/form/update.html', {'form':form})



# from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name
    
# class Region(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name
    
# class Product(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     image = models.ImageField(upload_to='products/', null=True, blank=True)

#     def __str__(self):
#         return self.name

# class Form(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     body = models.TextField()
#     is_checked = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

