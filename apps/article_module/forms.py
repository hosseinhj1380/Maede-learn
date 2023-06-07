# from django import forms
# from .models import Article,Comments
#
# class CommentForm (forms.ModelForm):
#
#     class Meta:
#         model = Comments
#         fields=['full_name','email','message']
#
#         widgets = {
#             'full_name': forms.TextInput(attrs={
#                 'class': "req",
#                 'placeholder': "نام و نام خانوادگی ",
#                 'name': 'name',
#                 'type': "text"
#             }),
#             'email': forms.TextInput(attrs={
#                 'class': "req",
#                 'placeholder': "ایمیل",
#                 'name': 'email',
#                 'type': "email"
#             }),
#             'message': forms.Textarea(attrs={
#                 'name': "name",
#                 'id': "message",
#                 'class': "req",
#
#                 'placeholder': "متن پیامتان را بنویسید",
#
#
#             })
#
#         }
#         labels = {
#             'full_name': 'نام و نام خانوادگی',
#             'email': 'ایمیل',
#             'message': 'پیام',
#
#         }
#     error_messages = {
#         'full_name': {
#             'required': 'لطفا نام و نام خانوادگی را به طور کامل وارد کنید ',
#         },
#         'email': {
#             'required': 'لطفا ایمیل خود را وارد کنید'
#         },
#         'message': {
#             'required': 'امکان ارسال پیام خالی وجود ندارد ',
#         },
#     }
