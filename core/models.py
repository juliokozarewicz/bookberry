from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class booksDataBase(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=250)
    dateRelease = models.DateField(default='')
    isbn = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)

    def get_absolute_url_delete(self):
        return reverse('core:delete', args=[self.pk])
    
    def get_absolute_url_edit(self):
        return reverse('core:edit', args=[self.pk])

    # Form is ok
    def get_absolute_url(self):
        return reverse('core:search')