from django.db import models
from django.utils import timezone
from hr_contacts import models as cm

class EmployeeModel(models.Model):
	name = models.CharField(max_length=20, verbose_name='Name')
	birthday = models.DateField(verbose_name='Birthday', default=timezone.now)
	street = models.CharField(max_length=200, verbose_name='Street')
	city = models.CharField(max_length=200, verbose_name='City')
	phone = models.CharField(max_length=20, verbose_name='Phone')
	zip_code = models.CharField(max_length=6, verbose_name='Zip Code')
	image = models.ImageField(upload_to='imgs/', default=None, null=True, blank=True)
	contact_id = models.ForeignKey(cm.ContactModel, on_delete=models.CASCADE, default=None)





