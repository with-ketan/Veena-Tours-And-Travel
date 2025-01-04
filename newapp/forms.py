from newapp.models import signup
from django import forms

class signupform(forms.ModelForm):
    class Meta:
        model = signup
        fields = "__all__"