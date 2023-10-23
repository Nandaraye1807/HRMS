from django import forms
from hr_jobs import models
from flatpickr import DatePickerInput

class JobCreateForm(forms.ModelForm):
	class Meta:
		model = models.JobModel
		fields = '__all__'

class JobUpdateForm(forms.ModelForm):
	class Meta:
		model = models.JobModel
		fields = '__all__'