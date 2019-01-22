from django import forms
from django.core.validators import RegexValidator

class userRegistration(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=35)
    business_type = forms.CharField(label='Business Type', max_length=15)
    mobile_validator = RegexValidator(message="Email ID must be entered in the format: abc@domain.com")
    mobile_number = forms.CharField(label='Mobile Number', max_length=10, validators=[mobile_validator])
    email_regex = RegexValidator(regex=r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message="Email ID must be entered in the format: abc@domain.com")
    email= forms.CharField(label='Email', validators=[email_regex], max_length=70)
    password= forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=15)

class userLogin(forms.Form):
    mobile_number = forms.CharField(label='Mobile Number', max_length=10)
    password= forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=15)
