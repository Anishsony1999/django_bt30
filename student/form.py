from django import forms
from django.contrib.auth.models import User
from .models import Student

class ContactForm(forms.Form):
    name = forms.CharField(label='Name',max_length=100,required=True)
    email = forms.EmailField(label='Email',max_length=100,required=True)
    add = forms.CharField(label='Add',max_length=200,required=True)

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='username',max_length=100,required=True)
    email = forms.EmailField(label='Email',max_length=100,required=True)
    password = forms.CharField(label='password',max_length=100,required=True)
    password_confirm = forms.CharField(label='password_confirm',max_length=100,required=True)

    class Meta:
        model = User
        fields = ['username','email','password']

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        password_confirm = clean_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password do not match")

class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=20,label='name',required=True) 
    age  = forms.IntegerField()
    add  = forms.CharField(max_length=100,label='add',required=True) 
    clas = forms.CharField(max_length=20,label='class',required=True) 

    class Meta:

        model = Student
        fields = ['name','age','add','clas']
    