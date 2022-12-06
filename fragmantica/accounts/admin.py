from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from fragmantica.accounts.forms import UserCreateForm, UserEditForm
from fragmantica.accounts.models import FragUser

UserModel=get_user_model()

@admin.register(UserModel)
class FragUserAdmin(UserAdmin):
	list_display = ('id', 'first_name', 'last_name', 'email', 'age')
	list_filter = ('first_name', 'last_name')
	search_fields = ('first_name', 'last_name','email',)
	sortable_by = ('id', 'first_name', 'last_name','email',)
	save_on_top=True


	form=UserEditForm
	add_form=UserCreateForm
	fieldsets = ((None,
				  {'fields': ('username', 'password',), }),
				 ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'gender'), },),
				 ('Permissions',
				  {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',), },),
				 ('Important dates', {'fields': ('last_login', 'date_joined',), },),)
