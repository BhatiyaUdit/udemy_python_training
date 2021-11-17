from django.contrib import admin
from .models import Posts

# Register your models here.
print("Inside blog >> admin.py ")


class PostAdminView(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')


admin.site.register(Posts, PostAdminView)
