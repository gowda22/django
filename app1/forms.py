
# NORMAL DJANGO FROM
from django import forms

#BUILT IN VALIDATION
# class ContactForm(forms.Form):

#     name = forms.CharField(max_length=100,required=True)

#     email = forms.EmailField()


# custom feild validation

# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField()
#     age = forms.IntegerField(min_value=18, max_value=79)

#     def clean_name(self):
#         entered_name = self.cleaned_data.get('name')

#         if entered_name.lower() == "admin":
#             raise forms.ValidationError("This name is not allowed")

#         return entered_name




# all in one
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18, max_value=79)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        entered_name = self.cleaned_data.get('name')

        if entered_name.lower() == "admin":
            raise forms.ValidationError("This name is not allowed")

        return entered_name

    def clean(self):
        cleaned_data = super().clean() #runs Django's normal form cleaning and gives you the cleaned field values.

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(
                    "Password and confirm password must match"
                )

        return cleaned_data

