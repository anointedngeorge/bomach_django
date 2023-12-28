from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    sub_title =  models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image =  models.ImageField(upload_to='slider', blank=True, null=True)
    is_active =  models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'

    def __str__(self) -> str:
        return f"{self.title} - {self.sub_title}"