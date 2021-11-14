from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, 'DRAFT'), (1, "PUBLISH"))


class Posts(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=True)

    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

