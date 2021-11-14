from django.apps import AppConfig

print("Inside blog >> apps.py ")


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
