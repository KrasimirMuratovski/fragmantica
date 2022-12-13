#awards./views.py
# from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from fragmantica.awards.models import Award


class AwardDetailsView(DetailView):
	template_name = 'awards/details-award.html'
	model = Award
	fields = ('name',)


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		try:
			context['awards_perfume'] = self.object.perfume
		except:
			context['awards_perfume'] = None

		return context


# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['is_owner'] = self.request.user == self.object
	#
	# 	return context


class AwardsListView(ListView):
	context_object_name = 'awards'
	template_name = 'awards/list-awards.html'
	model = Award
