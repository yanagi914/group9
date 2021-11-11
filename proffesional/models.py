from django.db import models

# Create your models here.
class My_Grades(models.Model):
    subject_name = models.CharField('科目名', blank=False, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    pass_or_fail = models.CharField('合否', blank=True, max_length=3)