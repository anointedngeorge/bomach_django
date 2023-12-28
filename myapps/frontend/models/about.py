from django.db import models


class About(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image =  models.ImageField(upload_to='slider', blank=True, null=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About us'

    def __str__(self) -> str:
        return f"About {self.title}"