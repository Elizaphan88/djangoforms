from django import forms


class HpStudentsForm(forms.Form):
    firstname = forms.CharField(max_length=30, label="Your First Name")
    lastname = forms.CharField(max_length=30, label="Your Last Name")
    email = forms.EmailField(max_length=50, label="Your Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Your Password")

