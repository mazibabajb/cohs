from django import forms
from.models import RegistrationForm


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = RegistrationForm
        fields = ['first_name','second_name','last_name']