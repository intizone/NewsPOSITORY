from django.urls import path
from .views import index, allnews, category, contact

urlpatterns = [
    path('', index, name='index'),
    path('allnews/', allnews, name='allnews'),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
]