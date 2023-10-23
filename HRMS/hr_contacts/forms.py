from django import forms
from hr_contacts import models
from flatpickr import DatePickerInput

class ContactCreateForm(forms.ModelForm):
	class Meta:
		model = models.ContactModel
		fields = '__all__'
		widgets = {
			'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
			'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
		}

class ContactUpdateForm(forms.ModelForm):
	class Meta:
		model = models.ContactModel
		fields = '__all__'
		widgets = {
			'start_date': DatePickerInput(options = {"dateFormat": "d.m.y",}),
			'end_date': DatePickerInput(options = {"dateFormat": "d.m.y",}),
		}





