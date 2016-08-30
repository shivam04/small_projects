from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
		model = User
		fields = ('username', 'email', 'password','first_name','last_name')
		widgets = {
		    'username': forms.TextInput(attrs={'class': 'form-control'}),
		    'email': forms.TextInput(attrs={'class': 'form-control'}),
		    'password': forms.PasswordInput(attrs={'class': 'form-control'}),
		    'first_name': forms.TextInput(attrs={'class': 'form-control'}),
		    'last_name': forms.TextInput(attrs={'class': 'form-control'}),
		}

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age', 'picture','gender')
        widgets = {
		    'age': forms.TextInput(attrs={'class': 'form-control'}),
		    'picture': forms.FileInput(attrs={'class': 'form-control'}),
		    'gender': forms.TextInput(attrs={'class': 'form-control'}),
		}