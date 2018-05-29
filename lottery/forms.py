from django import forms
from django.forms import TextInput

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'skype_telegram',]
        widgets = {
            'full_name': TextInput(attrs={'placeholder': 'Имя...'}),
            'email': TextInput(attrs={'placeholder': 'Email...'}),
            'skype_telegram': TextInput(attrs={'placeholder': 'Skype/Telegram...'}),

        }
        labels = {
            'full_name': 'Имя',
            'email': 'Email',
            'skype_telegram': 'Skype или Telegram',
        }

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        try:
            match = Client.objects.get(email=email)
        except Client.DoesNotExist:
            # Unable to find a user, this is fine
            return email

            # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already takes part.')


class CheckForm(forms.Form):
    unique_id = forms.CharField(required=False, max_length=9, label='')

    def __init__(self, *args, **kwargs):
        super(CheckForm, self).__init__(*args, **kwargs)
        self.fields['unique_id'].widget.attrs['placeholder'] = 'Введите ID'
