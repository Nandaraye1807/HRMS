from django import forms
from hr_employees import models
from flatpickr import DatePickerInput

class EmployeeCreateForm(forms.ModelForm):
	class Meta:
		model = models.EmployeeModel
		fields = '__all__'
		widgets = {
			'birthday': DatePickerInput(options = { "dateFormat": "d.m.y",}),
		}

class EmployeeUpdateForm(forms.ModelForm):
	class Meta:
		model = models.EmployeeModel
		fields = '__all__'
		widgets = {
			'birthday': DatePickerInput(options = { "dateFormat": "d.m.y",}),
		}