from django import forms
from hr_salary import models
from flatpickr import DatePickerInput

class SalaryCreateForm(forms.ModelForm):
    class Meta:
        model = models.SalaryModel
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }

class SalaryUpdateForm(forms.ModelForm):
    class Meta:
        model = models.SalaryModel
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }