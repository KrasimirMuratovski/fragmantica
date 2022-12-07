from django.contrib.auth import get_user_model
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
		# queryset=self.object.perfumepossession_set.all()
		# print(str(queryset.query))
		# context['your_perfumes']=self.object.perfumepossession_set.all()
		try:
			context['user_perfumes'] = self.object.perfumepossession_set.all()
		except:
			context['user_perfumes'] = None

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


class UserEditView(UpdateView):
	template_name='accounts/profile-edit-page.html'
	model=UserModel
	fields = ('username', 'first_name', 'last_name', 'gender', 'email')
	# success_url = reverse_lazy('details user' kwargs)

	def get_success_url(self):
		return reverse_lazy('details user', kwargs={'pk':self.request.user.pk, })


class UserDeleteView(DeleteView):
	template_name='accounts/profile-delete-page.html'
	model=UserModel
	success_url = reverse_lazy('index')
