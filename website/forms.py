from django import forms
from .models import UsersForm


class ContactForm(forms.ModelForm):
	class Meta:
		model = UsersForm
		fields = ['name','email','mobile','message']
