#accounts/model.py
from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

# We will use get_user_model() to access this class
from fragmantica.core.validators import validate_only_letters
from fragmantica.perfumes.models import Perfume


class ChoicesEnumMixin:
	@classmethod
	def gender_choices(cls):
		choices=[(x.name, x.value) for x in cls]
		return choices


	@classmethod
	def max_len(cls):
		return max(len(name) for name, _ in cls.gender_choices())



class Gender(ChoicesEnumMixin, Enum):
	male='Male'
	female='Female'
	NotSelected='Not Selected'



class FragUser(AbstractUser):
	MIN_LEN_NICK_NAME=2
	MAX_LEN_NICK_NAME=30
	MIN_LEN_FIRST_NAME=2
	MAX_LEN_FIRST_NAME=30
	MIN_LEN_LAST_NAME=2
	MAX_LEN_LAST_NAME=30

	nickname=models.CharField(unique=True, max_length=MAX_LEN_NICK_NAME, validators=(MinLengthValidator(MIN_LEN_NICK_NAME),validate_only_letters),null=True, blank=True)
	first_name=models.CharField(max_length=MAX_LEN_FIRST_NAME, validators=(MinLengthValidator(MIN_LEN_FIRST_NAME),validate_only_letters),)
	last_name=models.CharField(max_length=MAX_LEN_LAST_NAME, validators=(MinLengthValidator(MIN_LEN_LAST_NAME),validate_only_letters),)
	email=models.EmailField(unique=True, null=True, blank=True)
	age=models.PositiveIntegerField(null=True, blank=True)
	gender=models.CharField(choices=Gender.gender_choices(), max_length=Gender.max_len())
	perfume=models.ManyToManyField(Perfume)



#
#
# print(Gender.gender_choices())
# print(Gender.max_len())
