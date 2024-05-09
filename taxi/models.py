from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars",
    )

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.model}: {self.manufacturer}"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255, unique=True, blank=True, null=True
    )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}: {self.license_number}"
