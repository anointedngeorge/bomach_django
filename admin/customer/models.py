from django.db import models
import uuid
from authuser.models import User
from django.conf import settings
from django.urls import reverse

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
     related_name="customer_relationship")
    name = models.CharField(("name"), max_length=50)
    year = models.DateField(("Year"),auto_now_add=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Client"
        
    def __str__(self) -> str:
        return f"{self.name}"