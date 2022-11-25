from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from fragmantica.accounts.forms import UserCreateForm

UserModel=get_user_model()


def login_user(request):
	pass


class SignInView(LoginView):
	template_name='accounts/login-page.html'


class SignUpView(CreateView):
	template_name='accounts/register-page.html'
	form_class=UserCreateForm
	# model=UserModel
	# fields=('username', 'password')
	success_url = reverse_lazy('index')


