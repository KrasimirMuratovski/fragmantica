#common/models.py
from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from fragmantica.perfumes.models import Perfume

UserModel = get_user_model()

class PerfumeComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(max_length=MAX_TEXT_LENGTH,null=False,blank=False,)
    publication_date_and_time = models.DateTimeField(auto_now_add=True,null=False, blank=True,)
    perfume = models.ForeignKey(Perfume,on_delete=models.RESTRICT,null=False,blank=True,)
    user = models.ForeignKey(UserModel,on_delete=models.RESTRICT,)



class ChoicesEnumMixin:
    @classmethod
    def possession_choices(cls):
        choices=[(x.name, x.value) for x in cls]
        return choices

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.possession_choices())



class Possession(ChoicesEnumMixin, Enum):
    have_it='I have it'
    had_it='I had it'
    want_it='I want it'

class PerfumePossession(models.Model):
    possession = models.CharField(choices=Possession.possession_choices(), max_length=Possession.max_len())
    perfume = models.ForeignKey(Perfume,on_delete=models.RESTRICT,null=False,blank=True,)
    user = models.ForeignKey(UserModel,on_delete=models.RESTRICT,)