from django.urls import path, include

from fragmantica.designers.views import DesignerDetailsView, DesignerAddView, DesignerEditView, DesignerDeleteView

urlpatterns = (
		path('add/', DesignerAddView.as_view(), name='add designer'),
		path('<int:pk>/', include([
		path('', DesignerDetailsView.as_view(), name='details designer'),
		path('edit/', DesignerEditView.as_view(), name='edit designer'),
		path('delete/', DesignerDeleteView.as_view(), name='delete designer'),
			])),
)
	# path('profile/<int:pk>/',DesignerEditView.as_view(), name='edit designer' ),)