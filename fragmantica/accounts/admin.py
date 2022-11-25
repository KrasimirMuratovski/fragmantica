from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from fragmantica.accounts.models import FragUser

UserModel=get_user_model()

@admin.register(UserModel)
class FragUserAdmin(UserAdmin):
	pass