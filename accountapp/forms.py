from django.contrib.auth.forms import UserCreationForm
from django import forms

from accountapp.models import User


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True




# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(label='password', widget=forms.PasswordInput)
#     confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['nickname','email', 'profile']

class RegisterForm(forms.ModelForm):
    """ Create a new user """
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('nickname', 'email','profile')

    def clean_password(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')

        #if password1 and password1 != password2:
            #raise forms.ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.clean_password())
        if commit:
            user.save()
        return user