from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CreateCommentForm(forms.Form):
    comment  = forms.CharField(help_text='Enter a text comment, max length 400 chars ', max_length=400)
    def clean_comment(self):
        data = self.cleaned_data['comment']
        if len(data) > 400:
            raise ValidationError(_('Size of comment longer that 400 chars '))
        if not data:
            raise ValidationError(_('You can\'t post empty comment , sorry try agan !'))

        return data

