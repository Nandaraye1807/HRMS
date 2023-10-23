from django import forms
from hr_allowance import models
from flatpickr import DatePickerInput

class AllowanceCreateForm(forms.ModelForm):
    class Meta:
        model = models.AllowanceModel
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }

class AllowanceUpdateForm(forms.ModelForm):
    class Meta:
        model = models.AllowanceModel
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'end_date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }