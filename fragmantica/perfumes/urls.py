from django.urls import path, include

from fragmantica.perfumes.views import PerfumeListView, PerfumeDetailsView, comment_perfume, possession_perfume, \
	perfume_comment_edit, perfume_comment_delete, perfume_comment_view, perfumes_per_user_all

urlpatterns = (
	path('', PerfumeListView.as_view(), name='list perfumes'),
	path('<int:pk>/', PerfumeDetailsView.as_view(), name='details perfume'),
	#TODO - needed urls?
	path('posession/<int:perfume_id>/', possession_perfume, name='possession perfume'),
#TODO - edit_comment instead of comment?
	path('comment/<int:perfume_id>/', comment_perfume, name='comment perfume'),
	# path('edit/<int:perfume_id>/', perfume_comment_edit, name='perfume comment edit'),
	path('edit/<int:comment_id>/', perfume_comment_edit, name='perfume comment edit'),
	path('comment_view/<int:comment_id>/', perfume_comment_view, name='perfume comment view'),
	path('perfumes_per_user/<int:user_id>/', perfumes_per_user_all, name='perfumes per user all'),
	path('delete/<int:comment_id>/', perfume_comment_delete, name='perfume comment delete'),

		 )
