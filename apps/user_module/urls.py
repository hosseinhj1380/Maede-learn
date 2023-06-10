from django.urls import path
from . import views
from .views import UserPanelView, EditUserPanelView

app_name= "user"





urlpatterns = [
    path("user-panel",UserPanelView.as_view(),name="user-panel"),
    path("edit-user-panel",EditUserPanelView.as_view(),name="edit-user-panel"),
    path('sign-up', views.RegisterView.as_view(), name='register'),
    path('forget_password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('sign-in', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('reset_password/<str:activation_code>',views.ResetPasswordView.as_view(),name= "reset-password"),
    path('user-activation/<str:activation_code>',views.UserActivateView.as_view(),name= "user_activation")


    ]