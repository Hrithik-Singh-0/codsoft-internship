from django import forms
from .models import Contacts

class contact_book(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'phone', 'email', 'address']