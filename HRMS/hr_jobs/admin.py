from django.contrib import admin

# Register your models here.
from hr_jobs import models

class JobAdmin(admin.ModelAdmin):
	list_display = ['name', 'expected_employees']

admin.site.register(models.JobModel, JobAdmin)
