#perfumes/models.py
from datetime import date

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.utils.text import slugify

from fragmantica.awards.models import Award
from fragmantica.core.model_mixins import StrFromFieldsMixin
from fragmantica.designers.models import Designer
from fragmantica.notes.models import Note


class Perfume(StrFromFieldsMixin, models.Model):
	str_fields = ('name','year', )
	PERFUME_NAME_MAX_LEN=96
	PERFUME_NAME_MIN_LEN=2
	PERFUME_YEAR_MIN=1960
	PERFUME_YEAR_MAX=date.today().year#TODO - add auto year

	name=models.CharField(max_length=PERFUME_NAME_MAX_LEN, validators=(MinLengthValidator(PERFUME_NAME_MIN_LEN),), unique=True)
	year=models.IntegerField(validators=(MinValueValidator(PERFUME_YEAR_MIN),MaxValueValidator(PERFUME_YEAR_MAX),),)
	image = models.URLField(null=False,blank=False,)
	designer=models.ForeignKey(Designer, on_delete=models.RESTRICT,)
	note=models.ManyToManyField(Note,)
	award=models.OneToOneField(Award,on_delete=models.RESTRICT,null=True, blank=True,)
	slug = models.SlugField(unique=True, null=False, blank=True, )

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		if not self.slug:
			self.slug = slugify(f'{self.id}-{self.name}')

		return super().save(*args, **kwargs)
