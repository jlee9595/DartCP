from django import forms
from .models import Dept

DEPT_CHOICES = [[dept.id, dept] for dept in Dept.objects.all()]

class DeptFilterForm(forms.Form):
	filterdepts = forms.MultipleChoiceField(label='', choices=DEPT_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)

class SearchForm(forms.Form):
	search = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search'}))