from django.urls import path, include

from fragmantica.accounts.views import SignInView, SignUpView, SignOutView, UserDetailsView

urlpatterns=(
	# path('login/', login_user, name='login user'),
	path('login/', SignInView.as_view(), name='login user'),
	path('register/', SignUpView.as_view(), name='register user'),
	path('logout/', SignOutView.as_view(), name='logout user'),
	path('profile/<int:pk>', include(
		[
			path('', UserDetailsView.as_view(), name='details user'),
			# path('edit/', UserEditView.as_view(), name='edit user'),
			# path('delete/', UserDeleteView.as_view(), name='delete user'),

		 ]
	),
	#
	# path('profile/<int:pk>', UserDetailsView.as_view(), name='details user'),
	# path('profile/<int:pk>', UserDetailsView.as_view(), name='delete user'),
))