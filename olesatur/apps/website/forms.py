# -*- coding: utf-8 -*-
from django import forms

from olesatur.core.forms import FormMixin

class OrderForm(forms.Form, FormMixin):
    name = forms.CharField(label=u'Фамилия Имя', required=True,
        widget=forms.TextInput(attrs={'placeholder': u'Фамилия Имя'}))
    phone = forms.CharField(label=u'Телефон', required=False,
        widget=forms.TextInput(attrs={'class': 'vPhoneField', 'placeholder': u'Телефон для связи'}))
    email = forms.EmailField(label=u'Email', required=False,
        widget=forms.TextInput(attrs={'placeholder': u'Email'}))
    
    def clean(self):
        if not self.cleaned_data.get('phone') and not self.cleaned_data.get('email'):
            raise forms.ValidationError(u'Вы должны указать телефон либо email для связи с вами.')
        return self.cleaned_data

class CallbackForm(forms.Form, FormMixin):
    name = forms.CharField(label=u'Фамилия Имя', required=True,
        widget=forms.TextInput(attrs={'placeholder': u'Фамилия Имя'}))
    phone = forms.CharField(label=u'Телефон', required=True,
        widget=forms.TextInput(attrs={'class': 'vPhoneField', 'placeholder': u'Телефон для связи'}))
