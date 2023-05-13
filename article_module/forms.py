from django import forms
from .models import Article,Comments

class CommentForm (forms.ModelForm):

    class Meta:
        model = Comments
        fields=['text']

        widgets = {

            'text': forms.Textarea(attrs={
                'name': "name",
                'id': "message",
                'class': "req",
                'placeholder': "متن پیامتان را بنویسید",


            })

        }
        labels = {

            'text': 'پیام'

        }
    error_messages = {

        'text': {
            'required': 'امکان ارسال پیام خالی وجود ندارد ',
        },
    }
