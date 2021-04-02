from django import forms

from college.models import student

class studentmodelform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
