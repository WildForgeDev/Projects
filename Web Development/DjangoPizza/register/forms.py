from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    delivery_choices = [
        (1, 'Delivery'),
        (2, 'Carryout'),
    ]

    delivery_type = forms.ChoiceField(choices=delivery_choices, required=True,
                                      widget=forms.RadioSelect(attrs={'class': 'delivery_type'}))

    first_name = forms.CharField(max_length=50, required=True,
                                 widget=forms.TextInput(attrs={'class': 'first_name', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, required=True,
                                widget=forms.TextInput(attrs={'class': 'last_name', 'placeholder': 'Last Name'}))
    address = forms.CharField(max_length=75, required=True,
                              widget=forms.TextInput(attrs={'class': 'address', 'placeholder': 'Address'}))
    city = forms.CharField(max_length=50, required=True,
                           widget=forms.TextInput(attrs={'class': 'city', 'placeholder': 'City'}))
    state = forms.CharField(max_length=2, required=True,
                            widget=forms.TextInput(attrs={'class': 'state', 'placeholder': 'State'}))
    zip_code = forms.CharField(max_length=5, required=True,
                               widget=forms.TextInput(attrs={'class': 'zip_code', 'placeholder': 'Zip Code'}))
    phone_number = forms.IntegerField(required=True,
                                      widget=forms.TextInput(
                                          attrs={'class': 'phone_number', 'placeholder': 'Phone Number'}))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=25, required=True, widget=forms.TextInput(
        attrs={'class': 'username_field', 'placeholder': 'Enter a Username', 'id': 'username'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': 'email_field', 'placeholder': 'Email Address', 'id': 'email'}))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'password_field1', 'placeholder': 'Enter a password',
                                           'id': 'password1'}))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'password_field2', 'placeholder': 'Re-enter your password',
                                           'id': 'password2'}))

    class Meta:
        model = User
        fields = (
            'delivery_type', 'username', 'password1', 'password2', 'first_name', 'last_name', 'address', 'city',
            'state',
            'zip_code', 'email', 'phone_number')
