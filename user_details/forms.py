from django import forms
from .models import UserDetails


class UserProfileForm(forms.ModelForm):

    class Meta:
        fields = ['title', 'name', 'email', 'password', 'contact', 'address']
        model = UserDetails
        widgets = {
            'password': forms.PasswordInput()
        }
