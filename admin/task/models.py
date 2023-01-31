from django.db import models
import uuid
# Create your models here.

class Tasks(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable = False)
    name = models.CharField(("name"), max_length=50)
    year = models.DateField(("Year"),auto_now_add=True)

    class Meta:
        verbose_name = "Tasks"
        verbose_name_plural = "Tasks"
        
    def __str__(self) -> str:
        return f"{self.name}"