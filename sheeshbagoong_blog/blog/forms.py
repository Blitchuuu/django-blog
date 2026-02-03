from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'category', 'content',
            'featured_image', 'status', 'is_featured'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
