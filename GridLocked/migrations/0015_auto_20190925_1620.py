# Generated by Django 2.2.5 on 2019-09-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GridLocked', '0014_auto_20190925_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fighter',
            name='attribute',
        ),
        migrations.AddField(
            model_name='fighter',
            name='strong_vs',
            field=models.ManyToManyField(blank=True, to='GridLocked.Attribute'),
        ),
    ]
