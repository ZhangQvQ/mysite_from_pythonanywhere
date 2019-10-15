from django import forms
from comments.models import comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = ['name', 'email', 'url', 'text']
