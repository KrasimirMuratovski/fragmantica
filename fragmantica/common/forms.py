#common/forms
from django import forms


class SearchPerfumeForm(forms.Form):
    search_expression = forms.CharField(max_length=50,required=False,)

