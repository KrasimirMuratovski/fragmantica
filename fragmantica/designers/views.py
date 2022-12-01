#designers/views.py
# from django.urls import reverse_lazy
from django.views.generic import DetailView


from fragmantica.designers.models import Designer



class DesignerDetailsView(DetailView):
	template_name = 'designers/details-designer.html'
	model = Designer
	fields = ('name', 'photo', 'since')

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['is_owner'] = self.request.user == self.object
	#
	# 	return context


