#notes.urls.py
from django.urls import path

from fragmantica.notes.views import NoteDetailsView

urlpatterns = (
	path('<int:pk>/', NoteDetailsView.as_view(), name='details note'),
)
	# path('profile/<int:pk>/',DesignerEditView.as_view(), name='edit designer' ),)