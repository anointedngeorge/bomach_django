from django.db import models
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin,
    BaseUserManager,
    UserManager
)
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


GROUP_ROLES = [
    ('staff','Staff'),
    ('customer','Customer')
]

class CustomUserManager(UserManager):
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a vaild email address")

        email = self.normalize_email(email)
        user =  self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
        

class User(AbstractBaseUser, PermissionsMixin):
    code = models.CharField(max_length=300, blank=True, null=True)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(('email address'), unique=True, error_messages="Email Already Taken")
    username = models.CharField(max_length=300, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roles = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, related_name='roles_rel')
    roles_name = models.CharField(max_length=300, blank=True, choices=GROUP_ROLES, null=True)
    picture_url = models.CharField(max_length=300, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=timezone.now())
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_username(self):
        return f"{self.first_name} {self.last_name}"
        # return self.email
    
    def get_short_name(self):
        return f"{self.first_name} {self.last_name}" or self.email.split('@')[0]

    def natural_key(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        coded = str(uuid.uuid4()).replace("-", "")[:4]
        code = f"bom{coded}"
        self.code = code
        return super(User, self).save(*args, **kwargs)





# distinguise
class Staff(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
     related_name="related_staff")
    
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
        
    def __str__(self) -> str:
        return f"{self.user}"




class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
     related_name="related_customer")
    
    class Meta:
        verbose_name = "Customers"
        verbose_name_plural = "Customers"

    def __str__(self) -> str:
        return f"{self.user}"



class Branch(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    
    class Meta:
        verbose_name = "branch"
        verbose_name_plural = "branch"

    def __str__(self) -> str:
        return f"{self.name}"