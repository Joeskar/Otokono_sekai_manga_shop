from django.forms import ModelForm
from django import forms

from apps.blog.models import CommentBlog


class CommentForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control w-100',
               'rows': 9,
               'placeholder': 'Write Comment'}))

    class Meta:
        model = CommentBlog
        fields = ('content', )


