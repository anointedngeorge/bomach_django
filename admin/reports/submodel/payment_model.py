from django.db import models
from django.conf import settings
from customer.models import Customer



class ReportPayment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
     related_name="report_author_payment")
    client = models.ForeignKey(Customer,verbose_name='Client',  on_delete=models.CASCADE, null=True, blank=True,
     related_name="report_client")
    total_amount  = models.CharField(max_length = 150, null=True)
    CHOICE = [
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('reserve', 'Reserved'),
    ]

    status = models.CharField(max_length=500, null=True, default='pending', choices=CHOICE)
    created_at = models.DateField(auto_now=True)
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
    