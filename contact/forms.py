from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Your email address',
            'message': 'Message',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'border-black \
            rounded-lg profile-form-input'
        self.fields[field].label = False
