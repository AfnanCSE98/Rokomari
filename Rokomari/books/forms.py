from django import forms
import re
class UserForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={'class': 'input-group'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'input-group'}))
    confirm_password = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'input-group'}))
    mobile = forms.CharField( widget=forms.TextInput(attrs={'class': 'input-group'}))
    email = forms.CharField( widget=forms.TextInput(attrs={'class': 'input-group'}))
    address = forms.CharField( widget=forms.TextInput(attrs={'class': 'input-group'}))

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        mobile  = cleaned_data.get("mobile")
        email = cleaned_data.get("email")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password do not match"
            )
        for i in mobile:
            if not i.isalnum():
                raise forms.ValidationError(
                    "Provide a valid phone number"
                )
                break

        is_valid_mail = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))
        if not is_valid_mail:
            raise forms.ValidationError(
                "Provide a valid Email Address"
            )

class LoginForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())



class User_Profile_Form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    account_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))