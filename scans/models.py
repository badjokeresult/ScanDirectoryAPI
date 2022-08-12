from django.db import models

# Create your models here.


class Scan(models.Model):
    directory = models.CharField(verbose_name='Directory', max_length=150, blank=False, null=False)
    js_files = models.IntegerField(verbose_name='JS Files Processed')
    rmrf_files = models.IntegerField(verbose_name='rm -rf Files Processed')
    rundll_files = models.IntegerField(verbose_name='rundll Files Processed')
    errors = models.IntegerField(verbose_name='Errors Occured')
    execution_time = models.TimeField(verbose_name='Execution Time')
    is_completed = models.BooleanField(verbose_name='Is Checking Completed')