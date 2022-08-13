from django.db import models

# Create your models here.


class Scan(models.Model):
    directory = models.CharField(verbose_name='Directory', max_length=150, blank=False, null=False)
    js_files = models.IntegerField(verbose_name='JS Files Processed', blank=False)
    rmrf_files = models.IntegerField(verbose_name='rm -rf Files Processed', blank=False)
    rundll_files = models.IntegerField(verbose_name='rundll Files Processed', blank=False)
    errors = models.IntegerField(verbose_name='Errors Occured', blank=False)
    execution_time = models.CharField(verbose_name='Execution Time', max_length=150, blank=False)
    is_completed = models.BooleanField(verbose_name='Is Checking Completed', blank=False)