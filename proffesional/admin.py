from django.contrib import admin
from proffesional.models import My_Grades
from proffesional.models import Course_subject
from proffesional.models import System_subject
from proffesional.models import General_subject

# Register your models here.
admin.site.register(My_Grades)
admin.site.register(Course_subject)
admin.site.register(System_subject)
admin.site.register(General_subject)