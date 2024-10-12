from django.db import models
from django.urls import reverse

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    nicknames = models.CharField(max_length=200, blank=True)
    emoji_preference = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=50)
    tail = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    magical_properties = models.TextField(blank=True)
    image = models.ImageField(upload_to='cat_images/', default='default_cat.png')  # Add image field with default

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat_detail', args=[str(self.id)])
