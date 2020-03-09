from django import forms
from django.contrib.auth import forms as auth_forms


class LoginForm(auth_forms.AuthenticationForm):

    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={'autofocus': True}
        )
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password'}
        ),
    )
