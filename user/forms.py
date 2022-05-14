from django import forms
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter confirm password'})) 
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter first name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter last name'}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter first name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter last name'}), required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder': 'y-m-d'}), required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter city'}), required=False)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter about you'}), required=False)
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Enter mobile'}), required=False)
    class Meta:
        model = Profile
        fields = ['image', 'dob', 'gender', 'city', 'state', 'mobile', 'bio']


    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['state'].required = False
        self.fields['gender'].required = False
