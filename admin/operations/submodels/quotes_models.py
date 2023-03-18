from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class QuotesModel(models.Model):
    full_name = models.CharField(max_length = 150, null=True)
    email_address = models.CharField(max_length = 150, null=True)
    phone_number = models.CharField(max_length = 150, null=True)
    service = models.ForeignKey(to="settings.Service", 
    on_delete=models.CASCADE, related_name='service_rel', null=True)
    # service_category = models.ForeignKey(to="settings.Service", 
    # on_delete=models.CASCADE, related_name='service_category_rel', null=True)
    message = RichTextField()


    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'

    def __str__(self) -> str:
        return f"{self.full_name}"

    # def full_name(self, obj=None):
    #     print(obj)
    #     return self.full_name