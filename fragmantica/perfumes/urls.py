from django.urls import path, include

from fragmantica.perfumes.views import PerfumeListView, PerfumeDetailsView, comment_perfume, possession_perfume, \
	perfume_comment_edit, perfume_comment_delete, perfume_comment_view

urlpatterns = (
	path('', PerfumeListView.as_view(), name='list perfumes'),
	path('<int:pk>/', PerfumeDetailsView.as_view(), name='details perfume'),
	#TODO - needed urls?
	path('posession/<int:perfume_id>/', possession_perfume, name='possession perfume'),
	path('comment/<int:perfume_id>/', comment_perfume, name='comment perfume'),
	# path('edit/<int:perfume_id>/', perfume_comment_edit, name='perfume comment edit'),
	path('edit/<int:comment_id>/', perfume_comment_edit, name='perfume comment edit'),
	path('comment_view/<int:comment_id>/', perfume_comment_view, name='perfume comment view'),
	path('delete/<int:comment_id>/', perfume_comment_delete, name='perfume comment delete'),

		 )
