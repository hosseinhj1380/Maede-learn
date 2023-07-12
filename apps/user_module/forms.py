from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from apps.user_module.models import User


class RegisterForm(forms.Form):
    email = forms.CharField(label="ایمیل",
                            widget=forms.TextInput(attrs={
                                'class': "req",
                                'placeholder': "ایمیل",
                                'name': 'email',
                                'type': "email"
                            }))
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'signup-form',
            'type': "password",
            'placeholder': "رمـز عبـور",
        }))
    confirm_password = forms.CharField(
        label='تایید رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'signup-form',
            'type': "password",
            'placeholder': "تایید رمـز عبـور",
        }))

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     user: User = User.objects.filter(username__iexact=username)
    #
    #     if user :
    #         raise ValidationError('کاربری با این نام وجود دارد')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='آدرس ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'login-form',
            'type': "email",
            'placeholder': "آدرس ایمیل",

        }))
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'login-form',
            'type': "password",
            'placeholder': "رمـز عبـور",
        }))


class ForgetPassForm(forms.Form):
    email = forms.EmailField(
        label='آدرس ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'login-form',
            'type': "email",
            'placeholder': "آدرس ایمیل",

        }))


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'signup-form',
            'type': "password",
            'placeholder': "رمـز عبـور",
        }))
    confirm_password = forms.CharField(
        label='تایید رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'signup-form',
            'type': "password",
            'placeholder': "تایید رمـز عبـور",
        }))

class EditPanelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','number','avatar']
        username = forms.CharField(widget=forms.TextInput(attrs= {
            'class': "login-form",
            'placeholder': "نام کاربری  ",
            'name': 'name',
            'type': "text"
        }))
        widgets = {
            'first_name': forms.TextInput( attrs={
                'class': "req",
                'placeholder': "نام  ",
                'name': 'name',
                'type': "text"
            }),
            'last_name': forms.TextInput(attrs={
                'class': "req",
                'placeholder': "نام خانوادگی  ",
                'name': 'name',
                'type': "text"
            }),

            'number': forms.NumberInput(attrs={
                'class': "req",
                'placeholder': "شماره همراه ",
                'name': 'text',
                'type': "text"
            }),
            "avatar" : forms.FileInput()



        }
        labels = {
            'first_name': 'نام ',
            'last_name': ' نام خانوادگی',
            'username': ' نام کاربری',
            'number': 'شماره ی تلفن',
            'avatar' : 'آواتار',

        }


class EditPasswordForm(forms.Form):
    current_password = forms.CharField(
        label='رمز عبور فعلی ',
        widget=forms.PasswordInput(attrs={
            'class': 'signup-form',
            'type': "password",
            'placeholder': "رمـز عبـور فعلی ",
        }))
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'signup-form',
            'type': "password",
            'placeholder': "رمـز عبـور",
        }))
    confirm_password = forms.CharField(
        label='تایید رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'signup-form',
            'type': "password",
            'placeholder': "تایید رمـز عبـور",
        }))