from django import forms
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField

class userRegistration(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=35)
    business_type = forms.CharField(label='Business Type', max_length=15)
    mobile_number = forms.CharField(max_length=10)
    email_regex = RegexValidator(regex=r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message="Email ID must be entered in the format: abc@domain.com")
    email= forms.CharField(label='Email', validators=[email_regex], max_length=70)
    password= forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=15)
    def __init__(self, *args, **kwargs):
        super(userRegistration, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['business_type'].widget.attrs['placeholder'] = 'Business Type'
        self.fields['mobile_number'].widget.attrs['placeholder'] = 'Mobile Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class userFormLogin(forms.Form):
    mobile_validator = RegexValidator(message="Please enter valid mobile number")
    mobile_number = forms.CharField(validators=[mobile_validator], max_length=10)
    password= forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=15)

    def __init__(self, *args, **kwargs):
        super(userFormLogin, self).__init__(*args, **kwargs)
        self.fields['mobile_number'].widget.attrs['placeholder'] = 'Mobile Number'
        self.fields['password'].widget.attrs['placeholder']='Password'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
