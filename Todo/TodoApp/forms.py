from django.forms import ModelForm, fields
from .models import Todo,WorkDetails

class TodoForm(ModelForm):
    class Meta:
        model=Todo
        fields=['Work','studiesrelated']

class DetailsForm(ModelForm):
    class Meta:
        model=WorkDetails
        fields='__all__'