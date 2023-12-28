from django.db import models



LIST_DISPLAY_SETTINGS = ['system_title','system_phone','short_description']
class Settings(models.Model):
    system_title = models.CharField(max_length=300, null=True)
    system_phone =models.CharField(max_length=300, null=True)
    short_description = models.TextField(null=True)
    top_bar = models.ForeignKey("frontend.DataJosn", on_delete=models.CASCADE, 
                                related_name='top_bar_rel', blank=True, null=True)
    social_links = models.ForeignKey("frontend.DataJosn", on_delete=models.CASCADE, 
                                     related_name='social_links_rel', blank=True, null=True)
    logo = models.ImageField(upload_to='logo', blank=True, null=True)

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self) -> str:
        return f"{self.system_title}"
    
   

class DataJosn(models.Model):
    MENU = [
        ('top_bar','Top Bar'),
        ('social_links', 'Social Links')
    ]
    # settings = models.ForeignKey("frontend.Settings", on_delete=models.CASCADE)
    tag = models.CharField(max_length=150, choices=MENU, null=True)
    key = models.CharField(max_length=300, blank=True)
    value = models.CharField(max_length=300, blank=True)
    icon  = models.CharField(max_length=150, null=True, blank=True)


    class Meta:
        verbose_name = 'Extra data'
        verbose_name_plural = 'Extras data'

    def __str__(self) -> str:
        return f"{self.key}"