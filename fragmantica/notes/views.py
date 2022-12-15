#notes/views.py
# from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from fragmantica.notes.models import Note


class NoteDetailsView(DetailView):
	template_name = 'notes/details-note.html'
	model = Note
	fields = ('name', 'image', 'category', 'description')


#note/s must be put in the context/ManyToMany Relation
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['note_perfumes'] = self.object.perfume_set.all()

		return context

#TODO -remove
	# cart = Cart.objects.first()
	# objects = cart.cart_item.all()  # this line return all related objects for CartToys
	# # and in reverse
	# cart_toy = CartToys.objects.first()
	# carts = cart_toy.cart_set.all()  # this line return all related objects for Cart

# def get_context_data(self, **kwargs):
# 	context = super().get_context_data(**kwargs)
# 	context['is_owner'] = self.request.user == self.object
#
# 	return context


class NoteListView(ListView):
	context_object_name = 'notes'
	template_name = 'notes/list-notes.html'
	model = Note

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['notes_count'] = self.object_list.count()

		return context