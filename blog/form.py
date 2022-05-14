from django import forms
from . models import Post

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter description'}))
    content = forms.Textarea(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Content'}))

    class Meta:
        model = Post
        fields = ['image', 'category', 'title', 'description', 'content']