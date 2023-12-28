from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from customer.models import *
from human_resource.models import *



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_staff(sender, instance, created, *args, **kwargs):
    if created:
        role_name = instance.roles_name
        if role_name == 'customer':
            Customer.objects.all().create(user_id=instance.id)
        elif role_name == 'staff':
            Employee.objects.all().create(user_id=instance.id)
            filtered =  Employee.objects.all().filter(user_id=instance.id)
            if filtered.exists():
                Job_history.objects.all().create(employee_id=filtered.get().id)
                Salary.objects.all().create(employee_id=filtered.get().id)
                # Skill.objects.all().create(employee_id=filtered.get().id)
            else:
                print('No employee id found')
