#designers/views.py
# from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from fragmantica.designers.models import Designer



class DesignerDetailsView(DetailView):
	template_name = 'designers/details-designer.html'
	model = Designer
	fields = ('name', 'photo', 'since')


class DesignerListView(ListView):
	context_object_name = 'designers'
	template_name = 'designers/list-designers.html'
	model = Designer

