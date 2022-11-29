from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from fragmantica.accounts.forms import UserCreateForm

UserModel=get_user_model()

class UserDetailsView(DetailView):
	template_name='accounts/profile-details.html'
	model=UserModel

#TODO - contex data comes by default from 'DetailView'
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)

# TODO - adding field 'is_owner' or whatever
# TODO - self.object is the selected by pk // self.request.user is the logged in user
		context['is_owner']=self.request.user==self.object

		return context


class SignInView(LoginView):
	template_name='accounts/login-page.html'


class SignUpView(CreateView):

	template_name='accounts/register-page.html'
	form_class=UserCreateForm
	# model=UserModel
	# fields=('username', 'password')
	success_url = reverse_lazy('index')


class SignOutView(LogoutView):
	next_page=reverse_lazy('index')


# class UserEditView():
# 	pass