from django import forms
from models import Student


class StudentForm(forms.ModelForm):
	class Meta:
		fields = ['full_name', 'email']
		model = Student