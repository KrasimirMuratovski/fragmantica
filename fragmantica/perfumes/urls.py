from django.urls import path

from fragmantica.perfumes.views import PerfumeListView, PerfumeDetailsView, comment_perfume

urlpatterns = (
	path('', PerfumeListView.as_view(), name='list perfumes'),
	path('<int:pk>/', PerfumeDetailsView.as_view(), name='details perfume'),
	path('comment/<int:perfume_id>/', comment_perfume, name='comment perfume'),
)