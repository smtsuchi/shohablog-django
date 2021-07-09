from django import forms

# import our built-in form AND model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'content'
        ]

class CreateUserForm(UserCreationForm): # inherits from built-in
    class Meta:
        model = User
        # fields come from build-in User model. Read documentation
        # to see all availbale fields
        fields = ['username', 'email', 'password1', 'password2']
