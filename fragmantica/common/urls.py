from django.urls import path

from fragmantica.common.views import index

urlpatterns=(
	path('', index, name='index'),
	# # path('', SignInView.as_view(), name='login user'),
)