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
    # maybe this needs to be stored as a defensive profile will all attributes and a multiplier (rails seeds)
    tough_vs = models.ManyToManyField(to='Attribute', blank=True, related_name='+')
    weak_vs = models.ManyToManyField(to='Attribute', blank=True, related_name='+')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Equipment (models.Model):
    name = models.CharField(max_length = 250)
    weapon_range = models.PositiveIntegerField(default=0)
    force = models.IntegerField(default=0)
    attribute = models.ForeignKey(to='Attribute', on_delete=models.SET_NULL, null=True, blank=True)
    min_range_offest = models.PositiveIntegerField(default=0)
    area_of_effect = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Equipment'

class Attribute (models.Model):
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name


