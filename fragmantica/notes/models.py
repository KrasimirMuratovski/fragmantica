#notes/models.py
from datetime import date
from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from fragmantica.core.model_mixins import StrFromFieldsMixin, ChoicesEnumMixin


class Category(ChoicesEnumMixin, Enum):
    citrus = 'Citrus'
    musk = 'Musk'
    amber = 'Amber'
    woods_and_mosses = 'Woods and Mosses'
    herbs_and_fougeres = 'Herbs and Fougeres'
    uncategorized = 'Uncategorized'


class Note(StrFromFieldsMixin, models.Model):
	str_fields = ('name',)
	MIN_LEN_NAME=2
	MAX_LEN_NAME=96

	name=models.CharField(max_length=MAX_LEN_NAME, validators=(MinLengthValidator(MIN_LEN_NAME),),unique=True)
	image = models.URLField(null=False, blank=False, )
	slug = models.SlugField(unique=True, null=False, blank=True, )
	category = models.CharField(choices=Category.choices(),max_length=Category.max_len(),)
	description = models.TextField()

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		if not self.slug:
			self.slug = slugify(f'{self.id}-{self.name}')

		return super().save(*args, **kwargs)