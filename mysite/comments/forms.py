from django import forms
from comments.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = ['name', 'email', 'url', 'text']
