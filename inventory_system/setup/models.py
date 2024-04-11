from django.db import models

from django.db import models

class Inventory(models.Model):
    location_choices = [('Admin Office', 'Admin Office'), ('Room 01', 'Room 01'), ('Room 02', 'Room 02'),
                        ('Room 03', 'Room 03'), ('Room 04', 'Room 04'), ('Room 05', 'Room 05')]
    status_choices = [('Working', 'Working'), ('Not Working', 'Not Working')]

    date = models.DateField()
    number = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=20, choices=location_choices, null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"
