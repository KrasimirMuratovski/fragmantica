from django.urls import path, include

from fragmantica.designers.views import DesignerDetailsView, DesignerListView

urlpatterns = (
	path('', DesignerListView.as_view(), name='list designers'),
	path('<int:pk>/', DesignerDetailsView.as_view(), name='details designer'),
)
	# path('profile/<int:pk>/',DesignerEditView.as_view(), name='edit designer' ),)