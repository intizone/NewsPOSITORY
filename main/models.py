from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Form(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    body = models.TextField()
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

