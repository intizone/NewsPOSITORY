from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('allnews/', allnews, name='allnews'),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard/region/create', create_region, name='create_region'),
    path('dashboard/region/list', regions, name='regions'),
    path('dashboard/region/update/<int:id>/', region_update, name='region_update'),
    path('dashboard/region/delete/<int:id>/', region_delete, name='region_delete'),
    
    path('dashboard/category/create', create_category, name='create_category'),
    path('dashboard/category/list', categorys, name='categorys'),
    path('dashboard/category/update/<int:id>/', category_update, name='category_update'),
    path('dashboard/category/delete/<int:id>/', category_delete, name='category_delete'),
    
    
]