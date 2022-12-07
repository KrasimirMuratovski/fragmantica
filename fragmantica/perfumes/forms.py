from django import forms
#
# from petstagram.core.form_mixins import DisabledFormMixin
# from petstagram.pets.models import Pet

from fragmantica.common.models import PerfumeComment, PerfumePossession
from fragmantica.core.form_mixins import DisabledFormMixin


class PerfumeCommentForm(forms.ModelForm):
    class Meta:
        model = PerfumeComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={'cols': 40,'rows': 10,'placeholder': 'Add comment...'},),}


class PerfumePossessionForm(forms.ModelForm):
    class Meta:
        model = PerfumePossession
        fields = ('possession',)
        labels = {'possession': 'Change your relation:',}
        # widgets = {'possession': forms.Select()}
        # widgets = {'possession': forms.ModelChoiceField()}


class PerfumeCommentEditForm(forms.ModelForm):
    class Meta:
        model = PerfumeComment
        fields = ('text',)

#
class PerfumeCommentDeleteForm(DisabledFormMixin,forms.ModelForm):
    disabled_fields = ('text',)
    class Meta:
        model = PerfumeComment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


# #######################
# class PetBaseForm(forms.ModelForm):
#     class Meta:
#         model = Pet
#         # fields = '__all__' (not the case, we want to skip `slug`
#         fields = ('name', 'date_of_birth', 'personal_photo')
#         # exclude = ('slug',)
#         labels = {
#             'name': 'Pet Name',
#             'personal_photo': 'Link to Image',
#             'date_of_birth': 'Date of Birth',
#         }
#         widgets = {
#             'name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Pet name'
#                 }
#             ),
#             'date_of_birth': forms.DateInput(
#                 attrs={
#                     'placeholder': 'mm/dd/yyyy',
#                     'type': 'date',
#                 }
#             ),
#             'personal_photo': forms.URLInput(
#                 attrs={
#                     'placeholder': 'Link to image',
#                 }
#             )
#         }
#
#
# class PetCreateForm(PetBaseForm):
#     pass
#
#
# class PetEditForm(DisabledFormMixin, PetBaseForm):
#     disabled_fields = ('name',)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._disable_fields()
#
#
# class PetDeleteForm(DisabledFormMixin, PetBaseForm):
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
#

