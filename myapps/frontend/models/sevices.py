from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    icon = models.CharField(max_length=300, blank=True, null=True)
    note = models.TextField(null=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return f"{self.title}"