from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add in thumbnail later
    #add in author later

    #two steps after making a model will always be :
    #1. python manage.py makemigrations
    #2. python manage.py migrate


    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:70] + '...'