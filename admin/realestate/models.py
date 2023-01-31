from django.db import models
import uuid
# Create your models here.

# name = models.CharField(max_length=50)
#     classes = models.ForeignKey(Classes, verbose_name=_("Class"), null=True, on_delete=models.CASCADE, related_name="section")
#     date = models.DateField(auto_now=True)



class RealEstate(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable = False)
    name = models.CharField(max_length=500, null=True)
    total_amount = models.CharField(max_length=500, null=True)
    amount_deposited = models.CharField(max_length=500, null=True)
    unit_price = models.CharField(max_length=500, null=True)
    content = models.CharField(max_length=500, null=True)
    unique_code = models.CharField(max_length=500, null=True)
    is_blocked = models.BooleanField(default=False, null=True)
    is_featured = models.BooleanField(default=False, null=True)
    is_frontend = models.BooleanField(default=False, null=True)
    legal_fee = models.CharField(max_length=500, null=True)
    survey_plan = models.CharField(max_length=500, null=True)
    development_fee = models.CharField(max_length=500, null=True)
    created_at = models.DateField(auto_now=True)
    

    class Meta:
        verbose_name = "RealEstate"
        verbose_name_plural = "RealEstate"
        
    def __str__(self) -> str:
        return f"{self.name}"


class RealEstatePlot(models.Model):
    uuid = models.UUIDField(primary_key = True,
         default = uuid.uuid4, editable = False)
    
    realestate = models.ForeignKey("Realestate", verbose_name=("Realestate"), null=True, on_delete=models.CASCADE, related_name="realestate_rel")
    
    name = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=500, null=True)
    size = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=500, null=True)
    content = models.CharField(max_length=500, null=True)
    timer_date = models.CharField(max_length=500, null=True)
    timer = models.CharField(max_length=500, null=True)
    transactional_code = models.CharField(max_length=500, null=True)
    purchase_code = models.CharField(max_length=500, null=True)
    unique_code = models.CharField(max_length=500, null=True)
    resell_code = models.CharField(max_length=500, null=True)
    payment_id = models.CharField(max_length=500, null=True)
    is_blocked = models.BooleanField(default=False, null=True)
    is_featured = models.BooleanField(default=False, null=True)
    is_frontend = models.BooleanField(default=False, null=True)
    is_sold = models.BooleanField(default=False, null=True)