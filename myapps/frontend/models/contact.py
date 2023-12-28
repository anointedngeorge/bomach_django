from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=300, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self) -> str:
        return f"About {self.title}"