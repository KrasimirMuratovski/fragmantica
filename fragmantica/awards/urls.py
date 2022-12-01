#awards.urls.py
from django.urls import path

from fragmantica.awards.views import AwardDetailsView

urlpatterns = (
	path('<int:pk>/', AwardDetailsView.as_view(), name='details award'),
)
	# path('profile/<int:pk>/',DesignerEditView.as_view(), name='edit designer' ),)