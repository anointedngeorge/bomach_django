from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from plugins.dropdown import *



class QuotesModel(models.Model):
    # 100 Payment Pending
    # 200 70 percent payment
    # 300 Full payment
    # 400 payment was registered
    STATUS = [
        ("100", 'Pending'),
        ("200", 'Mininium Of 70 Percent'),
        ("300", 'Payment Completed'),
        ("400", 'Payment was rejected'),
    ]
    code = models.CharField(max_length = 150, null=True)
    customer = models.ForeignKey(to='customer.Customer', 
    on_delete=models.CASCADE,
    null=True,
    verbose_name='Client',
    related_name='customer_quote_rel')
    services = models.ForeignKey(to="settings.ServiceCalculator", 
                            on_delete=models.CASCADE, 
                            related_name='Service_calculator_rel', 
                            null=True)
    nb =  models.IntegerField(default=0, verbose_name='Number of bedroom')
    nf =  models.IntegerField(default=0, verbose_name='Number of floor')
    ns =  models.IntegerField(default=0, verbose_name='Number of sitting room')
    total = models.IntegerField(default=0)
    amount_deposited  = models.IntegerField(blank=True, null=True, default=0, verbose_name='Amount Deposited (70 Percent)')
    amount_pending  = models.IntegerField(blank=True, null=True, default=0, verbose_name="Amount Remaining")
    status = models.CharField(max_length = 150, default="100", choices=STATUS)
    comment  = models.TextField(default=True)
    

    class Meta:
        verbose_name = 'Service Quotes'
        verbose_name_plural = 'Service Quotes'

    def __str__(self) -> str:
        return f"{self.customer} - {self.nb} - {self.nf}"

    def get_fullname(self):
        return f"{self.services}"

    def natural_key(self):
        return self.__str__()

    def action(self):
        modalname = self._meta.model.__name__
        action = [
                # {"name":'Send Payment Confirmation', "href":f"payment-request-confirmation", "is_button":False, 
                # "query":{'id':self.id, 'code':self.code}},
                ]
                
        return singleDropdown(
            action=action,
            code=self.code, 
            modelname=modalname,
            report_template_name='tasks',
            is_report=False, 
            show_media=False,
            report_title='Employee',
            link='/admin/reports/get-report'
        )