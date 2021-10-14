from django import forms
from .models import *


class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields='__all__'
