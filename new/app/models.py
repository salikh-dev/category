from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    class Meta:
        verbose_name  = "My Users"
        verbose_name_plural = "My Users"
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey('Category',blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
