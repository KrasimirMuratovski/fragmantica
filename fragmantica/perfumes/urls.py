from django.urls import path, include

from fragmantica.perfumes.views import PerfumeListView, PerfumeDetailsView, comment_perfume, possession_perfume, \
	perfume_comment_edit

urlpatterns = (
	path('', PerfumeListView.as_view(), name='list perfumes'),
	path('<int:pk>/', PerfumeDetailsView.as_view(), name='details perfume'),
	path('posession/<int:perfume_id>/', possession_perfume, name='possession perfume'),
	path('comment/<int:perfume_id>/', include([
		path('', comment_perfume, name='comment perfume'),
		path('edit/', perfume_comment_edit, name='perfume comment edit'),
												]
											)
		 ),

			)
