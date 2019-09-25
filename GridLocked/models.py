from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

class Fighter (models.Model):
    name = models.CharField(max_length = 250)
    max_health = models.PositiveIntegerField(default=0)
    general = models.ForeignKey(to=User, on_delete=models.CASCADE)
    left_equip = models.ForeignKey('Equipment', null=True, on_delete=models.SET_NULL, related_name='+')
    right_equip = models.ForeignKey('Equipment', null=True, on_delete=models.SET_NULL, related_name='+')
    back_equip = models.ForeignKey('Equipment', null=True, on_delete=models.SET_NULL, related_name='+')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Equipment (models.Model):
    name = models.CharField(max_length = 250)
    weapon_range = models.PositiveIntegerField(default=0)
    damage = models.PositiveIntegerField(default=0)
    attribute = models.CharField(max_length = 250, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Equipment'

