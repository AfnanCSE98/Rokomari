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


class UserProfileForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-group'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    account_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))

class AddElectronicsForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    model = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    image_src = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    warranty = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    number_of_items_added = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))

class UpdateElectronicsForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    model = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    warranty = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    number_of_items_added = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))

class AddBrandForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    web_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    image_src = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))

class AddElectronicsCategoryForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    image_src = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))


class Addbook_Form(forms.Form):
    ISBN = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Edition = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    No_of_Pages = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Country = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Language = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Price = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Image_src = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Summary = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Author = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Category = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Publisher = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    Stock = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))

class AddAuthor_Form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    profile = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))

class AddPublisher_Form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    web_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))

class AddCategory_Form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group'}))

