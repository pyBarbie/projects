from django.forms import ModelForm, Textarea
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'status',)

        widgets = {
            'title' : Textarea(attrs={'cols': 10, 'rows': 10}),
            'body' : Textarea(attrs={'cols': 15 , 'rows': 10})
        }