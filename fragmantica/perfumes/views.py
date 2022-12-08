#designers/views.py
# from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from fragmantica.common.models import PerfumeComment
from fragmantica.perfumes.forms import PerfumeCommentForm, PerfumePossessionForm, PerfumeCommentEditForm, \
    PerfumeCommentDeleteForm
from fragmantica.perfumes.models import Perfume

UserModel=get_user_model()


class PerfumeDetailsView(DetailView):
    context_object_name = 'perfume'
    template_name = 'perfumes/details-perfume.html'
    model = Perfume
    fields = ('name', 'year', 'image', 'designer', 'note')

#note/s must be put in the context/ManyToMany Relation
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfume_notes'] = self.object.note.all()
        context['perfume_comments'] = self.object.perfumecomment_set.all()
        context['request_user']= self.request.user
        context['comment_form'] = PerfumeCommentForm()
        context['possession_form'] = PerfumePossessionForm()
        try:
            context['perfume_possession'] = self.object.perfumepossession_set.get().possession
        except:
            context['perfume_possession'] ='Not defined yet.'

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
        comment.perfume = perfume#Attach the related perfume
        comment.user = request.user#Attach the related user
        comment.save()
    return redirect('index')



@login_required
def possession_perfume(request, perfume_id):
    perfume = Perfume.objects.filter(pk=perfume_id).get()
    perfume.perfumepossession_set.all().delete()
    form = PerfumePossessionForm(request.POST)

    if form.is_valid():
        posession=possession_perfume
        print(posession)
        possession = form.save(commit=False)  # Does not persist to DB
        possession.perfume = perfume
        possession.user = request.user
        possession.save()
    return redirect('details perfume', perfume_id)




@login_required
def perfume_comment_edit(request, comment_id):
    comment=PerfumeComment.objects.get(pk=comment_id)
    # perfume_id=comment.perfume.pk
    if request.method == 'GET':
        form = PerfumeCommentEditForm(instance=comment)
    else:
        form = PerfumeCommentEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            # return redirect('details perfume', pk=perfume_id)
            return redirect('index')

    context = {'form': form, 'comment':comment, 'comment_id':comment_id}
    return render(request, 'perfumes/perfume-comment-edit.html', context)



@login_required
def perfume_comment_view(request, comment_id):
    comment=PerfumeComment.objects.get(pk=comment_id)
    # perfume_id=comment.perfume.pk
    if request.method == 'GET':
        form = PerfumeCommentEditForm()
    else:
        form = PerfumeCommentEditForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('details perfume', pk=perfume_id)
            return redirect('index')

    context = {'form': form, 'comment':comment, 'comment_id':comment_id}
    return render(request, 'perfumes/perfume-comment-view.html',context)



@login_required
def perfume_comment_delete(request, comment_id):
    comment=PerfumeComment.objects.get(pk=comment_id)
    # perfume_id=comment.perfume.pk
    if request.method == 'GET':
        form = PerfumeCommentDeleteForm(instance=comment)
    else:
        form = PerfumeCommentDeleteForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            # return redirect('details perfume', pk=perfume_id)
            return redirect('index')

    context = {'form': form, 'comment':comment, 'comment_id':comment_id}
    return render(request, 'perfumes/perfume-comment-delete.html', context)




# TODO:remove/ context:
# context['logged_in'] = self.object.perfumecomment_set.all()
# user = self.object.fraguser_set.get()
# context['is_owner']=user == self.request.user.pk
# context['is_owner']=user == self.request.user
# queryset=self.object.perfumecomment_set.all()
# print(str(queryset.query))

# queryset=self.object.fraguser_set.all()
# print(str(queryset.query))
# print(str(queryset.query.username))

# perf_comment = self.object.perfumecomment_set.all().
# print(perf_comment.t)

# context['is_owner'] = self.request.user == self.object
# context['user_id'] = self.user.pk
# profile.user = request.user
# user_id = request.user.pk,


# current_user=self.object.fraguser_set
# print(current_user)
# queryset=self.object.fraguser_set.all().values('password')
# print(str(queryset.query))
# print(str(queryset))
# print(str(queryset.query.username))