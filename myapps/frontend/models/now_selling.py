from django.db import models


class NowSelling(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='now_selling')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Now Selling'
        verbose_name_plural = 'Now Sellings'

    def __str__(self) -> str:
        return f"{self.title}"