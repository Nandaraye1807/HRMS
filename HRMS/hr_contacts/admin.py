from django.contrib import admin

# Register your models here.
from hr_contacts import models

class ContactAdmin(admin.ModelAdmin):

	list_display = ['name','start_date','end_date',]

admin.site.register(models.ContactModel, ContactAdmin)
