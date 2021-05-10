from django import forms
from .models import Post
from .models import uploadPost

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover']

class uploadPostForm(forms.ModelForm):
    class Meta:
        model = uploadPost
        fields =['imagesname', 'findimages']

