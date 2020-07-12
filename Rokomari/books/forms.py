from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-group', 'placeholder': 'NAME'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'input-group',
                                                                           'placeholder': 'PASSWORD'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'input-group',
                                                                                   'placeholder': 'CONFIRM PASSWORD'}))

    mobile = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-group',
                                                                     'placeholder': 'MOBILE NO'}))

    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-group',
                                                                    'placeholder': 'EMAIL ID'}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-group', 'placeholder': 'ADDRESS'}))

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password do not match"
            )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()