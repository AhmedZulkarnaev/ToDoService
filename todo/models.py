import time
import hashlib
from django.conf import settings
from django.db import models

from .utils import generate_pk


class Category(models.Model):
    id = models.CharField(max_length=16, primary_key=True, default=generate_pk, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.CharField(max_length=16, primary_key=True, default=generate_pk, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='tasks', blank=True)

    def __str__(self):
        return self.title
    
    def get_deadline_display(self):
        """Возвращает строку с дедлайном или 'Без срока'"""
        return self.deadline.strftime('%Y-%m-%d') if self.deadline else "Без срока"