#common/forms
from django import forms
from fragmantica.common.models import PerfumeComment

##TODO remove#}
# class PerfumeCommentForm(forms.ModelForm):
#     class Meta:
#         model = PerfumeComment
#         fields = ('text',)
#         widgets = {
#             'text': forms.Textarea(
#                 attrs={
#                     'cols': 40,
#                     'rows': 10,
#                     'placeholder': 'Add comment...'
#                 },
#             ),
#         }


class SearchPerfumeForm(forms.Form):
    perfume_name = forms.CharField(
        max_length=50,
        required=False,
    )
