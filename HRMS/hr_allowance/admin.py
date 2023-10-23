from django.contrib import admin

from hr_allowance import models

class AllowanceAdmin(admin.ModelAdmin):
	
	list_display = ['name', 'start_date', 'end_date']

admin.site.register(models.AllowanceModel, AllowanceAdmin)
# Register your models here.
