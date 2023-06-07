from django.urls import path
from . import views

app_name= "user"
urlpatterns = [
    path('sign-up', views.RegisterView.as_view(), name='register'),
    path('forget_password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('sign-in', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('reset_password/<str:activation_code>',views.ResetPasswordView.as_view(),name= "reset-password"),
    path('user-activation/<str:activation_code>',views.UserActivateView.as_view(),name= "user_activation")


    ]