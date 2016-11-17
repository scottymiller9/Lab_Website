from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Your name', max_length=100, required=True)
    contact_email = forms.EmailField(label='Your email', max_length=100, required=True)
    your_message = forms.CharField(label='Your message', min_length=20, required=True, widget=forms.Textarea)
