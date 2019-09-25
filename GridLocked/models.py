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
    # this needs to be stored as a defensive profile will all attributes and a multiplier (rails seeds)
    tough_vs = models.ManyToManyField(to='Attribute', blank=True, related_name='+')
    weak_vs = models.ManyToManyField(to='Attribute', blank=True, related_name='+')
    # also might need an attack profile

    # ideally there would be a mechanism for a procedurally generated attack profile
    # and the same for a defense profile. Perhaps with a power factor of "1", the totals
    # of the profiles would be generated based on an average of "1". For example, given
    # a potential damage set of [lava,steel,energy,cold] an attack profile could be
    # [1.2, 0.8, 0.5, 1.5] and a defense profile could be [2.0, 0.4, 0.4, 1.2]. Incoming 
    # and outgoing damage would be multiplied by the corresponding value. These would 
    # have max bounds and randomized, making the opportunity for a player finding the 
    # "perfect" robot for a goal or to match equipment. The table size needs to scale
    # with the number of attributes.

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


