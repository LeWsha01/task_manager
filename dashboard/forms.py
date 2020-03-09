from django import forms
from django.contrib import auth


class ConstuctUsForm(forms.Form):
    name = forms.CharField(
        help_text='Your first and last name.'
    )
    email = forms.EmailField(
        help_text='Email to contant you.'
    )
    message = forms.CharField(
        initial='My problem is...',
        help_text='Describe your issue here.',
        widget=forms.Textarea,
        # required=False,
    )

    def clean_email(self):
        data = self.cleaned_data['email']
        if auth.get_user_model().objects.filter(email=data).exists():
            raise forms.ValidationError(
                'Seems like you already have an account in the system.')
        return data
