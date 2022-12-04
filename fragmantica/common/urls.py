from django.urls import path

from fragmantica.common.views import index

urlpatterns=(
	path('', index, name='index'),
	# path('comment/<int:perfume_id>/', comment_perfume, name='comment perfume'),
	# # path('', SignInView.as_view(), name='login user'),
)