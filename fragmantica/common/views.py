from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

#
#Initial Index
# def index(request):
# 	return render(request, 'common/index.html')
#
from fragmantica.common.forms import SearchPerfumeForm
from fragmantica.perfumes.models import Perfume

def index(request):
    search_form = SearchPerfumeForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['perfume_name']

    perfumes = Perfume.objects.all()

    if search_pattern:
        perfumes = perfumes.filter(name__icontains=search_pattern)
    context = {
        'perfumes': perfumes,
        # 'comment_form': PerfumeCommentForm(),
        'search_form': search_form,
    }

    return render(
        request,
        'common/index.html',
        context,
    )
