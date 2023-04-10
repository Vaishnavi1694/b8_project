from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ("name",)    # for single field
        fields = "__all__"       # here we can mention whatever field we want as we want all field from models.py
        # exclude = ("is_active",)


# created by html
# class BookForm(forms.Form):
   
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
#     password = forms.CharField(widget = forms.PasswordInput())

# print(BookForm())

from django import forms

STATES = (
    ('', 'Choose...'),
    ('MH', 'Maharashtra'),
    ('MP', 'Madhya Pradesh'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),   
    ('DL', 'Delhi')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)