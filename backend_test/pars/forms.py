# coding=utf-8
from django import forms
from .models import UrlModel
# class UrlForm(forms.ModelForm):
#     class Meta():
#         model = UrlModel
#         fields = ('success','title','charset')
#         widgets = {
#             'success': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
#             'title':forms.Textarea(attrs={'cols': 10, 'rows': 5}),
#             'charset':forms.Textarea(attrs={'cols': 10, 'rows': 5})
#         }


class UrlForm(forms.Form):
    # два окна  TextArea   из задания
    table1 = forms.CharField(widget=forms.Textarea)
    table2 = forms.CharField(widget=forms.Textarea)
