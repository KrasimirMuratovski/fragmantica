from django.urls import path

from fragmantica.accounts.views import SignInView, SignUpView

urlpatterns=(
	# path('login/', login_user, name='login user'),
	path('login/', SignInView.as_view(), name='login user'),
	path('register/', SignUpView.as_view(), name='register user'),
)