#common/forms
from django import forms

class SearchPerfumeForm(forms.Form):
    search_expression = forms.CharField(max_length=50,required=False,)

#
# class UserEditForm(UserChangeForm):
#     class Meta:
#         model = UserModel
#         fields = "__all__"
#         field_classes = {"username": UsernameField}
#
# class UserCreateForm(UserCreationForm):
#     #we need to overwrite meta of the parrent UserCreationForm
#     class Meta:
#         model = UserModel
#         fields = ("username","email")
#         field_classes = {"username": UsernameField}

