from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	# first_name = forms.CharField(max_length=30, required=False, help_text='optional')
	# last_name  = forms.CharField(max_length=30, required=False, help_text="optional")
	email      = forms.EmailField(max_length=254, help_text="Required.")
	class meta:
		model = User
		fields = ('username','email', 'password1')