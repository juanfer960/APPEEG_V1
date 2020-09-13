from django import forms
from django.core import validators
from .models import User


class FormName(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    mail = forms.EmailField()


    class Meta:
        model = User
        fields = '__all__'



class NewUserForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        all_clean_data = super().clean()
        name = all_clean_data['name']
        password = all_clean_data['password']


class FormSearch(forms.Form):

    doctor = forms.CharField()
    paciente = forms.CharField()

    def clean(self):
        all_clean_data = super().clean()
        doctor = all_clean_data['doctor']
        paciente = all_clean_data['paciente']

