from decimal import Decimal

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from pizzapp.models import Cart


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
    last_name = forms.CharField(required=True, max_length=50)
    from_email = forms.EmailField(required=True, max_length=50)
    subject = forms.CharField(required=True, max_length=150)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=2000)


class CareersForm(forms.Form):
    position = forms.CharField(required=True, max_length=50,
                               widget=forms.TextInput(attrs={'class': 'position', 'placeholder': 'Position'}))
    first_name = forms.CharField(required=True, max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'first_name', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, max_length=50,
                                widget=forms.TextInput(attrs={'class': 'last_name', 'placeholder': 'Last Name'}))
    from_email = forms.EmailField(required=True, max_length=50,
                                  widget=forms.TextInput(attrs={'class': 'from_email', 'placeholder': 'Email Address'}))
    phone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'phone_number', 'placeholder': 'Phone Number'}))
    resume = forms.CharField(required=True, max_length=3000,
                             widget=forms.TextInput(attrs={'class': 'resume', 'placeholder': 'Resume'}))


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomerForm(forms.Form):
    delivery_choices = [
        (1, 'Delivery'),
        (2, 'Carryout'),
    ]

    delivery_type = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=delivery_choices)

    first_name = forms.CharField(required=True, max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'first_name', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, max_length=50,
                                widget=forms.TextInput(attrs={'class': 'last_name', 'placeholder': 'Last Name'}))
    address = forms.CharField(required=True, max_length=150,
                              widget=forms.TextInput(attrs={'class': 'address', 'placeholder': 'Street Address'}))
    city = forms.CharField(required=True, max_length=50,
                           widget=forms.TextInput(attrs={'class': 'city', 'placeholder': 'City'}))
    state = forms.CharField(required=True, max_length=2,
                            widget=forms.TextInput(attrs={'class': 'state', 'placeholder': 'State'}))
    zip_code = forms.CharField(required=True, max_length=5,
                               widget=forms.TextInput(attrs={'class': 'zip', 'placeholder': 'Zip'}))
    email = forms.EmailField(required=True, max_length=50,
                             widget=forms.TextInput(attrs={'class': 'email', 'placeholder': 'Email Address'}))
    phone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'phone_number', 'placeholder': 'Phone Number'}))
