#designers/views.py
# from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from fragmantica.perfumes.forms import PerfumeCommentForm
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
        context['perfume_notes'] = self.object.note.all()
        context['comment_form'] = PerfumeCommentForm()
        # context['is_owner'] = self.request.user == self.object
        # context['user_id'] = self.user.pk
        # profile.user = request.user
        # user_id = request.user.pk,

        return context




class PerfumeListView(ListView):
    context_object_name = 'perfumes'
    template_name = 'perfumes/list-perfumes.html'
    model = Perfume



@login_required
def comment_perfume(request, perfume_id):
    perfume = Perfume.objects.filter(pk=perfume_id).get()

    form = PerfumeCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)  # Does not persist to DB
        comment.perfume = perfume
        comment.user = request.user
        comment.save()

    return redirect('index')
