from django.db import models

# Create your models here.
class data(models.Model):
    date = models.DateField(auto_now_add=True,)
    title = models.TextField()
    content = models.TextField()