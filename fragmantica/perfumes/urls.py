from django.urls import path

from fragmantica.perfumes.views import PerfumeListView, PerfumeDetailsView

urlpatterns = (
	path('', PerfumeListView.as_view(), name='list perfumes'),
	path('<int:pk>/', PerfumeDetailsView.as_view(), name='details perfume'),
)