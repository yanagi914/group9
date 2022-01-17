from django.db import models

# Create your models here.
#自分の成績
class My_Grades(models.Model):
    subject_name = models.CharField('科目名', blank=False, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    pass_or_fail = models.IntegerField('合否', blank=True, default=0)
    isCheckedFlag = models.BooleanField('チャック済みかの判定',default=False)

#コース科目 A群
class Course_A_subject(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#コース科目 B群
class Course_B_subject(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#コース科目 C群
class Course_C_subject(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#一般教養科目 外国語科目
class General_foreignlang_subject(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#一般教養科目 外国語科目 サブ
class General_foreignlang_subject_sub(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#一般教養科目 地域連携科目
class General_local_subject(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#一般教養科目 地域連携科目 サブ
class General_local_subject_sub(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#一般教養科目 人と社会に関する科目
class General_human_subject(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#一般教養科目 人と社会に関する科目 サブ
class General_human_subject_sub(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#学部・学科共通科目 理工学部共通科目
class System_common_subject(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#学部・学科共通科目 理工学部共通科目 サブ
class System_common_subject_sub(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#学部・学科共通科目 システム理化学科共通科目
class System_subject(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)

#学部・学科共通科目 システム理化学科共通科目 サブ
class System_subject_sub(models.Model):
    subject_name = models.CharField('科目名', blank=True, max_length=100)
    subject_code = models.CharField('授業コード', blank=False, max_length=10)
    credit = models.FloatField('単位数',blank=False,default=0)
    compulsory_or_elective = models.CharField('必修・選択', blank=True, max_length=100)