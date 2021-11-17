from . import views
from django.urls import path

print("Inside blog >> urls.py ")

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_pattern'),
    path("about/", views.AboutView.as_view(), name="about_view_pattern")
]
