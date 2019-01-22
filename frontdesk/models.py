from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class userSignUp(models.Model):
    full_name = models.CharField('Full Name', max_length=35)
    business_type = models.CharField('Business Type', max_length=15)
    mobile_number = models.CharField('Mobile Number', max_length=10, unique=True)
    email_regex = RegexValidator(regex=r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message="Email ID must be entered in the format: abc@domain.com")
    email= models.CharField('Email', validators=[email_regex], max_length=70)
    password= models.CharField('Password', max_length=15)

    def __str__(self):
        return self.full_name


class userLogin(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be entered in the format: '9999 9999 99'.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    password = models.CharField(max_length=25)

    def __str__(self):
        return str(self.mobile_number)+" : "+self.password
