#common/forms
from django import forms

from fragmantica.common.models import PerfumeComment


class SearchPerfumeForm(forms.Form):
    search_expression = forms.CharField(max_length=50,required=False,)




































#
# class PetEditForm(DisabledFormMixin, PetBaseForm):
#     disabled_fields = ('name',)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._disable_fields()
#
#
# class PerfumeCommentDeleteForm(forms.ModelForm):
#     class Meta:
#         model = PerfumeComment
#     disabled_fields = ('name', 'date_of_birth', 'personal_photo')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._disable_fields()
#
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.delete()
#         return self.instance
