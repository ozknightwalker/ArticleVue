from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    @property
    def detail_url(self):
        return reverse('homepage')

    def detail_url_not(self):
        return reverse('homepage')
