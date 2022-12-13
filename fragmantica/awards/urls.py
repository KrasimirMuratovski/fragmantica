#awards.urls.py
from django.urls import path

from fragmantica.awards.views import AwardDetailsView, AwardsListView

urlpatterns = (
	path('<int:pk>/', AwardDetailsView.as_view(), name='details award'),
	path('', AwardsListView.as_view(), name='list awards'),

)
	# path('profile/<int:pk>/',DesignerEditView.as_view(), name='edit designer' ),)