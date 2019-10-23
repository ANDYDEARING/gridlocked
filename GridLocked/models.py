from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from django.core.validators import MinValueValidator
from decimal import *

class Fighter (models.Model):
    name = models.CharField(max_length = 250)
    max_health = models.PositiveIntegerField(default=0)
    general = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    left_equip = models.ForeignKey('Equipment', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    right_equip = models.ForeignKey('Equipment', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    back_equip = models.ForeignKey('Equipment', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    energy_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal(0.00))])
    acid_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal(0.00))])
    metal_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal(0.00))])
    quantum_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal(0.00))])

    def __str__(self):
        return f"{self.name} - E:{self.energy_value} A:{self.acid_value} M:{self.metal_value} Q:{self.quantum_value}"

    class Meta:
        ordering = ['name']

class Equipment (models.Model):
    name = models.CharField(max_length = 250)
    weapon_range = models.PositiveIntegerField(default=0)
    force = models.IntegerField(default=0)
    ATTRIBUTE_CHOICES = [
        ('E', 'ENERGY'),
        ('A', 'ACID'),
        ('M', 'METAL'),
        ('Q', 'QUANTUM')
    ]
    attribute = models.CharField(max_length=1, choices= ATTRIBUTE_CHOICES, default='E')
    min_range_offest = models.PositiveIntegerField(default=0)
    area_of_effect = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Equipment'