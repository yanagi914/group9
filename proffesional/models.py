from django.db import models

# Create your models here.
class My_Grades(models.Model):
    subject_name = models.CharField('科目名', blank=False, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    pass_or_fail = models.CharField('合否', blank=True, max_length=3)

class Course_subject(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)