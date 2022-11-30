#designers.forms.py
from django import forms

from fragmantica.designers.models import Designer


class DesignerCreateForm(forms.ModelForm):
	class Meta:
		model=Designer
		fields=('name','photo', 'since')