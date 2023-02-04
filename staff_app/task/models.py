from django.db import models
import uuid
# Create your models here.

class Tasks(models.Model):
    # id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)
    name = models.CharField(("name"), max_length=50)
    year = models.DateField(("Year"),auto_now_add=True)
    task_title= models.CharField(max_length=255, null=True)
    priority = models.CharField(max_length=500, null=True)
    start_date = models.CharField(max_length=500, null=True)
    end_date = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = "Tasks"
        verbose_name_plural = "Tasks"
        
    def __str__(self) -> str:
        return f"{self.name}"