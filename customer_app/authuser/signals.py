from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from authuser.models import *



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_staff(sender, instance, created, *args, **kwargs):
    if created:
        print(instance.roles_name)

        # Staff.objects.create(user=instance)