from django.shortcuts import render
from .models import Posts
from django.views.generic import DetailView

print("Inside blog >> views.py ")


# Create your views here.

# # lecture 280 Adding views

class BlogView(DetailView):
    print("inside Blog View Class")
    model = Posts
    template_name = "blog.html"
