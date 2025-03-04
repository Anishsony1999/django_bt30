from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name',max_length=100,required=True)
    email = forms.EmailField(label='Email',max_length=100,required=True)
    add = forms.CharField(label='Add',max_length=200,required=True)

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='username',max_length=100,required=True)
    email = forms.EmailField(label='Email',max_length=100,required=True)
    password = forms.CharField(label='password',max_length=200,required=True)
    password_confirm = forms.CharField(label='password_confirm',max_length=200,required=True)