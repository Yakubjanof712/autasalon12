from django.db import models

# Create your models here.
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brend nomi")
    country = models.CharField(max_length=100, verbose_name="Ishlab chiqaruvchi mamlakat")

    def __str__(self):
        return self.name
class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name="Mashina nomi")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    year = models.PositiveIntegerField(verbose_name="Yili")
    photo = models.ImageField(upload_to='car_photos/', null=True, blank=True, verbose_name="Mashina rasmi")

    def __str__(self):
        return f"{self.brand.name} - {self.name}"
