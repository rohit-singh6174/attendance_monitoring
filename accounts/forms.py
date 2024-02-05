from django import forms
from .models import Account
from django.core.validators import MinLengthValidator, MaxLengthValidator

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=8,widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }),
    )
    
    confirm_password = forms.CharField(max_length=8,widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }),
    )

    phone_number = forms.CharField(max_length=10)


    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')

        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
           raise forms.ValidationError("Password does not Match")


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
    )