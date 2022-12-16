#designers/views.py
# from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from fragmantica.common.models import PerfumeComment, PerfumePossession
from fragmantica.perfumes.forms import PerfumeCommentForm, PerfumePossessionForm, PerfumeCommentEditForm, \
    PerfumeCommentDeleteForm
from fragmantica.perfumes.models import Perfume

UserModel=get_user_model()


class PerfumeDetailsView(DetailView):
    context_object_name = 'perfume'
    template_name = 'perfumes/details-perfume.html'
    model = Perfume
    fields = ('name', 'released', 'image', 'designer', 'note')

#note/s must be put in the context/ManyToMany Relation
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfume_notes'] = self.object.note.all()
        context['perfume_comments'] = self.object.perfumecomment_set.all()
        context['request_user']= self.request.user
        context['comment_form'] = PerfumeCommentForm()
        context['possession_form'] = PerfumePossessionForm()
        possession_dict={'have_it':'I have it',
                        'had_it':'I had it',
                        'want_it':'I want it',
                         'not_defined_yet':'Not defined yet.',
                        }
        try:
            possession = self.object.perfumepossession_set.get().possession
        except:
            possession ='not_defined_yet'
        context['perfume_possession']=possession_dict[possession]

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
    return redirect('details perfume', perfume_id)



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
    perfume_id=comment.perfume_id
    if request.method == 'GET':
        form = PerfumeCommentEditForm(instance=comment)
    else:
        form = PerfumeCommentEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            # return redirect('details perfume', pk=perfume_id)
            # return redirect('index')
            return redirect('details perfume', perfume_id)

    context = {'form': form, 'comment':comment, 'comment_id':comment_id}
    return render(request, 'perfumes/perfume-comment-edit.html', context)


##########Created 08/12/2022AM#############

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

##########Created 08/12/2022AM#############
@login_required
def perfume_comments_per_user_all(request, user_id):
    user_comments=PerfumeComment.objects.filter(user_id=user_id)
    # user=User.objects.all().get(pk=user_id)
    # user_comments=user.perfumecomment_set.all()
    context = {'user_comments':user_comments, }
    return render(request, 'perfumes/perfume-comments-per-user-all.html',context)
#####################


##########Created 08/12/2022AM#############
@login_required
def perfumes_per_user_all(request, user_id):
    user_perfume_objects = []
    user_possession_ids=PerfumePossession.objects.filter(user_id=user_id)#queryset of the possession for user
    for user_perfume_id in user_possession_ids:
        # print(user_perfume_id.id)
        # print(user_perfume_id.perfume_id)
        perfume=Perfume.objects.filter(pk=user_perfume_id.perfume_id).get()
        user_perfume_objects.append(perfume)
        # print(perfume.name)
    # print(user_perfume_ids)

    # user=User.objects.all().get(pk=user_id)
    # user_comments=user.perfumecomment_set.all()
    context = {'user_perfume_objects':user_perfume_objects, 'user_id':user_id }
    return render(request, 'perfumes/perfumes-per-user-all.html',context)
#####################



@login_required
def perfume_comment_delete(request, comment_id):
    comment=PerfumeComment.objects.get(pk=comment_id)
    perfume_id=comment.perfume_id
    if request.method == 'GET':
        form = PerfumeCommentDeleteForm(instance=comment)
    else:
        form = PerfumeCommentDeleteForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('details perfume', perfume_id)
            # return redirect('index')

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