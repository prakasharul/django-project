from django import forms

from . models import projects


class projectForm(forms.ModelForm):

	target_date =forms.DateTimeInput()	
	class Meta:
		model = projects
		fields = ('name','client','budget','mobile','email','resource','duration','target_date')
