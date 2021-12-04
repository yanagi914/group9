from django.contrib import admin
from proffesional.models import My_Grades
from proffesional.models import Course_A_subject
from proffesional.models import Course_B_subject
from proffesional.models import Course_C_subject
from proffesional.models import System_subject
from proffesional.models import System_common_subject
from proffesional.models import General_foreignlang_subject
from proffesional.models import General_local_subject
from proffesional.models import General_human_subject

# Register your models here.
admin.site.register(My_Grades)
admin.site.register(Course_A_subject)
admin.site.register(Course_B_subject)
admin.site.register(Course_C_subject)
admin.site.register(System_subject)
admin.site.register(System_common_subject)
admin.site.register(General_foreignlang_subject)
admin.site.register(General_local_subject)
admin.site.register(General_human_subject)