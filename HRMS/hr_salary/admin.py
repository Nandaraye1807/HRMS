from django.contrib import admin

# Register your models here.
from hr_salary import models

class SalaryAdmin(admin.ModelAdmin):

    list_display = ['name','start_date','end_date']

admin.site.register(models.SalaryModel, SalaryAdmin)