from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

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
		context['user_pk']=self.request.user.pk
		try:
			context['user_perfumes'] = self.object.perfumepossession_set.all()
		except:
			context['user_perfumes'] = None

		try:
			context['user_comments'] = self.object.perfumecomment_set.all()
		except:
			context['user_comments'] = None


		return context


class SignInView(LoginView):
	template_name='accounts/login-page.html'


class SignUpView(CreateView):

	template_name='accounts/register-page.html'
	form_class=UserCreateForm
	# model=UserModel
	# fields=('username', 'password')
	success_url = reverse_lazy('index')
	# success_url = reverse_lazy('login user')

	def post(self, request, *args, **kwargs):
		response = super().post(request, *args, **kwargs)
		login(request, self.object)
		return response

class SignOutView(LogoutView):
	next_page=reverse_lazy('index')


class UserEditView(UpdateView):
	template_name='accounts/profile-edit-page.html'
	model=UserModel
	fields = ('username', 'first_name', 'last_name', 'gender', 'email', 'avatar')
	# success_url = reverse_lazy('details user' kwargs)

	def get_success_url(self):
		return reverse_lazy('details user', kwargs={'pk':self.request.user.pk, })


class UserDeleteView(DeleteView):
	template_name='accounts/profile-delete-page.html'
	model=UserModel
	success_url = reverse_lazy('index')
