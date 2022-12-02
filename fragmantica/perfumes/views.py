#designers/views.py
# from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from fragmantica.perfumes.models import Perfume


class PerfumeDetailsView(DetailView):
	context_object_name = 'perfume'
	template_name = 'perfumes/details-perfume.html'
	model = Perfume
	fields = ('name', 'year', 'image', 'designer', 'note')

#note/s must be put in the context/ManyToMany Relation
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# perfume_notes=
		context['perfume_notes'] = self.object.note.all()
		# context['perfume_award'] = self.object.note.all()

		return context

#TODO -remove
	# cart = Cart.objects.first()
	# objects = cart.cart_item.all()  # this line return all related objects for CartToys
	# # and in reverse
	# cart_toy = CartToys.objects.first()
	# carts = cart_toy.cart_set.all()  # this line return all related objects for Cart




class PerfumeListView(ListView):
	context_object_name = 'perfumes'
	template_name = 'perfumes/list-perfumes.html'
	model = Perfume

