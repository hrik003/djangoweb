import email
from tkinter.tix import Form
from turtle import title
from django import forms

class contactForm(forms.Form):
    fname = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'fname-input form-control', 'placeholder':'First Name'}))
    lname = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'lname-input form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={'class':'email-input form-control', 'placeholder':'Email'}))
    phone = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'phone-input form-control', 'placeholder':'Phone'}))
    message = forms.CharField(label='', required=False, widget=forms.Textarea(attrs={'class':'message-input form-control form-control-sm', 'placeholder':'Message'}))