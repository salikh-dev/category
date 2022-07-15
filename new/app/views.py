from django.shortcuts import render
from .models import *

def home(request):
    categories = request.GET.get("category")
    if categories == None:
        post = Post.objects.all()
    else:
        post = Post.objects.filter(category__category_name=categories)
        
    category = Category.objects.all()
    context = {
        "category":category,
        "post":post
    }
    return render(request, 'index.html', context)
