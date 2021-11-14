from django.shortcuts import render
from .models import Posts
from django.views.generic import DetailView


# Create your views here.

# # lecture 280 Adding views

class BlogView(DetailView):
    model = Posts
    template_name = "blog.html"
