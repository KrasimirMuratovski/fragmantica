from django.urls import path

from fragmantica.common.views import index, about

urlpatterns=(
	path('', index, name='index'),
	path('about/', about, name='about'),
	# path('comment/<int:perfume_id>/', comment_perfume, name='comment perfume'),
	# # path('', SignInView.as_view(), name='login user'),
)