from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name',max_length=100,required=True)
    email = forms.EmailField(label='Email',max_length=100,required=True)
    add = forms.CharField(label='Add',max_length=200,required=True)
    