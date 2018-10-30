from django import forms
from django.contrib.admin.widgets import AdminDateWidget


from . models import projects


class projectForm(forms.ModelForm):

	target_date =forms.CharField(widget=AdminDateWidget())	
	class Meta:
		model = projects
		fields = ('name','client','budget','mobile','email','resource','duration','target_date')
