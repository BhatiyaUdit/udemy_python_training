from django.shortcuts import render
from .models import Posts
from django.views.generic import DetailView, TemplateView, ListView

print("Inside blog >> views.py ")


# Create your views here.

# # lecture 280 Adding views

class BlogView(DetailView):
    print("inside Blog View Class")
    model = Posts
    template_name = "blog.html"


class AboutView(TemplateView):
    template_name = "about.html"


class HomeView(ListView):
    # for desc order add 'minus -' symbol in orderby
    queryset = Posts.objects.filter(status=1).order_by('date_created')
    print("QUERY SET ------>", queryset)
    template_name = "index.html"
