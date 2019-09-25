from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

class Fighter (models.Model):
    name = models.CharField(max_length = 250)
    max_health = models.PositiveIntegerField(default=0)
    left_equip = models.
    right_equip = 
    back_equip = 


    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    correct_answer = models.OneToOneField(to="Answer", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    times_favorited = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Equipment (models.Model):
    name = 
