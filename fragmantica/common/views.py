from django.shortcuts import render

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
        perfumes = perfumes.filter(tagged_pets__name__icontains=search_pattern)

    # photos = [apply_likes_count(photo) for photo in photos]
    # photos = [apply_user_liked_photo(photo) for photo in photos]
    # print(photos)
    context = {
        'perfumes': perfumes,
        # 'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }

    return render(
        request,
        'common/index.html',
        context,
    )

#
# @login_required
# def like_photo(request, photo_id):
#     user_liked_photos = PhotoLike.objects \
#         .filter(photo_id=photo_id, user_id=request.user.pk)
#
#     if user_liked_photos:
#         user_liked_photos.delete()
#     else:
#         PhotoLike.objects.create(
#             photo_id=photo_id,
#             user_id=request.user.pk,
#         )
#
#     return redirect(get_photo_url(request, photo_id))
#
#
# @login_required
# def comment_photo(request, photo_id):
#     photo = Photo.objects.filter(pk=photo_id) \
#         .get()
#
#     form = PhotoCommentForm(request.POST)
#
#     if form.is_valid():
#         comment = form.save(commit=False)  # Does not persist to DB
#         comment.photo = photo
#         comment.save()
#
#     return redirect('index')
#

#
# def share_photo(request, photo_id):
#     photo_details_url = reverse('details photo', kwargs={
#         'pk': photo_id
#     })
#     pyperclip.copy(photo_details_url)
#     return redirect(get_photo_url(request, photo_id))
#
