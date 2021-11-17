from . import views
from django.urls import path

print("Inside blog >> urls.py ")

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_pattern'),
    path("", views.HomeView.as_view(), name="home_view_pattern")
]
