from django import forms 

from .models import list

from django.forms import ModelForm

class ListForm(forms.ModelForm): 
      class Meta:
          model = list
          fields = "__all__"
          

          






