#designers/views.py
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DetailView, DeleteView

from fragmantica.designers.forms import DesignerCreateForm
from fragmantica.designers.models import Designer


class DesignerAddView(CreateView):
	template_name='designers/add-designer.html'
	model = Designer
	# form_class = DesignerCreateForm
	fields = ('name', 'photo', 'since')

	success_url = reverse_lazy('index')


class DesignerDetailsView(DetailView):
	template_name = 'designers/details-designer.html'
	model = Designer
	fields = ('name', 'photo', 'since')

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['is_owner'] = self.request.user == self.object
	#
	# 	return context


class DesignerEditView(UpdateView):
	template_name='designers/designer-edit-page.html'
	model=Designer
	fields = ('name', 'photo', 'since')

	def get_success_url(self):
		return reverse_lazy('details designer', kwargs={'pk':self.request.designer.pk, })
	#
	# def get_success_url(self):
	# 	return reverse_lazy('index')

#
#
# class SignUpView(CreateView):
#
# 	template_name='accounts/register-page.html'
# 	form_class=UserCreateForm
# 	# model=UserModel
# 	# fields=('username', 'password')
# 	success_url = reverse_lazy('index')
#
#


class DesignerDeleteView(DeleteView):
	template_name='accounts/designer-delete-page.html'
	model=Designer
	success_url = reverse_lazy('index')
