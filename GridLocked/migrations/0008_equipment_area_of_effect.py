# Generated by Django 2.2.5 on 2019-09-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GridLocked', '0007_equipment_min_range_offest'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='area_of_effect',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
