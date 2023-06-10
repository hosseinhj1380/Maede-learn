from django.contrib.auth import login, logout
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import CreateView
from django.views.generic.base import View, TemplateView
from utils.email_service import send_mail
from apps.user_module.forms import RegisterForm, LoginForm, ForgetPassForm, ResetPasswordForm, EditPanelForm
from apps.user_module.models import User


# Create your views here.


class UserPanelView(TemplateView):
    template_name = "user_module/user-panel.html"

def user_panel_components(request):
    return  render(request,"user_module/user-components/user-panel-component.html",context={})


class EditUserPanelView(View):
    def get(self,request):
        form = EditPanelForm()
        context = {
            "form": form
        }
        return render(request, "user_module/edit-user-panel.html",context)

    def post(self,request):
        return render(request, "user_module/edit-user-panel.html", {})
class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        login_form = LoginForm()
        context = {
            "register_form": register_form
        }
        return render(request, 'user_module/register_form.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email_user = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user: bool = User.objects.filter(email__iexact=email_user).first()

            if user:
                form.add_error("email", 'حسابی با این مشخصات موجود است')
            else:
                new_user = User(email=email_user, activation_code=get_random_string(5), is_active=False,
                                username=email_user)
                new_user.set_password(password)
                new_user.save()
                send_mail("ایمیل فعال سازی",{"user" : user},"user_module/email/activate_mail.html",new_user.email,)
                return redirect(reverse('user:login'))
        context = {
            "register_form": form
        }
        return render(request, 'user_module/register_form.html', context)


class UserActivateView(View):
    def get(self, request, activation_code):
        user: User = User.objects.get(activation_code__iexact=activation_code)
        if not user.is_active:
            if user:
                user.is_active = True
                user.save()
                return redirect(reverse('user:login'))
            raise Http404
        else:  # todo : user is already active !
            pass


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'user_module/login_form.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home:home_page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'user_module/login_form.html', context)


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse("home:home_page"))

class ForgetPasswordView(View):
    def get(self, request):
        forget_pass_form = ForgetPassForm()
        context = {
            "forget_form": forget_pass_form
        }
        return render(request, "user_module/forget_password.html", context)

    def post(self, request):
        forget_pass_form = ForgetPassForm(request.POST)
        if forget_pass_form.is_valid():
            email = forget_pass_form.cleaned_data.get("email")
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None :
                forget_pass_form.add_error("email", "کاربری با این ایمیل وجود ندارد")
            send_mail("ایمیل فعال سازی", {"user": user}, "user_module/email/reset_code.html", user.email )
            return redirect(reverse("user:reset-password"))

        context = {
            "forget_form": forget_pass_form
        }
        return render(request, "user_module/forget_password.html", context)



class ResetPasswordView(View):
    def get(self, request: HttpRequest, activation_code):
        user: User = User.objects.filter(activation_code__iexact=activation_code).first()
        if user is None:
            return redirect(reverse('user:login'))

        reset_pass_form = ResetPasswordForm()

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'user_module/reset_password.html', context)

    def post(self, request: HttpRequest, activation_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(activation_code__iexact=activation_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('user:login'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.activation_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('user:login'))

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }

        return render(request, 'user_module/reset_password.html', context)