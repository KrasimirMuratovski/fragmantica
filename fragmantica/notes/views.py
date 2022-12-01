#notes/views.py
# from django.urls import reverse_lazy
from django.views.generic import DetailView

from fragmantica.notes.models import Note


class NoteDetailsView(DetailView):
	template_name = 'designers/details-designer.html'
	model = Note
	fields = ('name', 'photo', 'since')

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['is_owner'] = self.request.user == self.object
	#
	# 	return context


