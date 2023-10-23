from django.db import models

# Create your models here.
from django.utils import timezone
from hr_jobs import models as jm

class SalaryModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    start_date = models.DateField(verbose_name='Start Date', default=timezone.now)
    end_date = models.DateField(verbose_name='End Date', default=timezone.now)
    salary = models.FloatField(verbose_name='Salary', default=0.0)
    job_id = models.ManyToManyField(jm.JobModel)

    def __str__(self):
        return self.name