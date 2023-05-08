from django import forms
from .models import ContactUs


# class ContactUsForm(forms.Form):
#     full_name = forms.CharField(label='نام و نام خانوادگی',
#                                 widget=forms.TextInput(attrs={
#                                     'class': "form-control",
#                                     'placeholder': "نام و نام خانوادگی ",
#                                     'name': 'message',
#                                     'type': "text"
#                                 }), )
#     subject = forms.CharField(label='عنوان',
#                               error_messages={
#                                   'required': 'please enter the full name'
#                               },
#                               widget=forms.TextInput(attrs={
#                                   'class': "form-control",
#                                   'placeholder': "عنوان ",
#                                   'name': 'subject',
#                                   'type': "text"
#                               }),
#                               )
#     email = forms.CharField(label='ایمیل',
#                             error_messages={
#                                 'required': 'please enter the full name'
#                             },
#                             widget=forms.TextInput(attrs={
#                                 'class': "form-control",
#                                 'placeholder': "ایمیل",
#                                 'name': 'message',
#                                 'type': "emial"
#                             }),
#                             )
#     text = forms.CharField(label='متن پیام', required=True,
#                            error_messages={
#                                'required': 'please enter the full name'
#                            },
#                            widget=forms.Textarea(attrs={
#                                'name': "message",
#                                'id': "message",
#                                'class': "form-control",
#                                'rows': "8",
#                                'placeholder': "پیغـام شمـا",
#                                'cols': 'None'
#                            }),
#                            )


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'title', 'email', 'message','site']
        widgets = {
            'full_name': forms.TextInput( attrs={
                'class': "req",
                'placeholder': "نام و نام خانوادگی ",
                'name': 'name',
                'type': "text"
            }),
            'email': forms.TextInput(attrs={
                'class': "req",
                'placeholder': "ایمیل",
                'name': 'email',
                'type': "email"
            }),
            'site': forms.TextInput(attrs={
                'class': "",
                'placeholder': "https://",
                'name': 'site',
                'type': "text"
            }),
            'title': forms.TextInput(attrs={
                'class': "req",
                'placeholder': "موضوع ",
                'name': 'site',
                'type': "text"
            }),
            'message': forms.Textarea(attrs={
                'name': "name",
                'id': "message",
                'class': "req",
                'rows': "8",
                'placeholder': "متن پیامتان را بنویسید",
                'cols': 'None'

            })

        }
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'title': 'موضوع',
            'email': 'ایمیل',
            'message': 'پیام',
            "site" : "وبسایت"
        }
        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی را به طور کامل وارد کنید ',
            },
            'email' : {
                'required': 'لطفا ایمیل خود را وارد کنید'
        },
            'title': {
                'required': 'عنوان پیام خود را وارد کنید ',
            },
            'message': {
                'required': 'امکان ارسال پیام خالی وجود ندارد ',
            },
        }
