from django import forms
from authuser.models.user import VendorOtherBusiness



class vendorBusinessForm(forms.ModelForm):
    
    class Meta:
        model = VendorOtherBusiness
        fields = [
                    "vendor_owner",
                    # "first_name",
                    # "last_name",
                    "vendor_name",
                    "country",
                    "state",
                    "city",
                    "weekOpeningHours",
                    "weekClosingHours",
                    "satOpeningHours",
                    "satClosingHours",
                    "sunWeekOpeningHours",
                    "sunWeekClosingHours",
                    "address",
                    "shop_name",
                    "shop_type",
                    "shop_image",
                    "balance",
                    "longitude",
                    "latitude",
                    "profileLogo",
                    "personalId",
                    "businessId",
                    "businessBio",
                ]

        