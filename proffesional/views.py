from django.shortcuts import redirect,render
from . import models
import csv
from io import TextIOWrapper, StringIO

def title(request):
    template_file = "proffesional/title.html"

    option = {

    }
    return render(request, template_file, option)


def result(request):
    template_file = "proffesional/result.html"

    option = {

    }
    return render(request, template_file, option)

def main(request):
    error_message = []
    mode = "SIRS"
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='ansi')
        csv_file = csv.reader(form_data)

        csv_list = [row for row in csv_file]

        if csv_list[0][1] == "開講年度":
            mode = "SIRS"
        elif csv_list[0][1] == "科目大区分":
            mode = "kakuteiseiseki"
        
        # csvからモデルMy_Gradesにデータを追加
        for index,line in enumerate(csv_list):
            if index < 4:
                continue
            else:
                if mode == "SIRS":
                    my_grades, created =models.My_Grades.objects.get_or_create(subject_name=line[4])
                    my_grades.subject_name = line[4]
                    my_grades.subject_code = line[3]
                    if line[7] == "合":
                        my_grades.pass_or_fail = 1
                    else:
                        my_grades.pass_or_fail = 0
                    my_grades.save()
                elif mode == "kakuteiseiseki":
                    my_grades, created =models.My_Grades.objects.get_or_create(subject_name=line[4])
                    my_grades.subject_name = line[4]
                    if line[10] == "合":
                        my_grades.pass_or_fail = 1
                    else:
                        my_grades.pass_or_fail = 0
                    my_grades.save()

            if mode == "SIRS":
                my_grades, created =models.My_Grades.objects.get_or_create(subject_name=line[4])
                my_grades.subject_name = line[4]
                my_grades.subject_code = line[3]
                if line[7] == "合":
                    my_grades.pass_or_fail = 1
                else:
                    my_grades.pass_or_fail = 0
                my_grades.save()
            elif mode == "kakuteiseiseki":
                my_grades, created =models.My_Grades.objects.get_or_create(subject_name=line[4])
                my_grades.subject_name = line[4]
                if line[10] == "合":
                    my_grades.pass_or_fail = 1
                else:
                    my_grades.pass_or_fail = 0
                my_grades.save()
        #自分の成績をリストに格納
        My_Grade_list = models.My_Grades.objects.all()
        #単位数データをリストに格納
        Course_A_subject_list = models.Course_A_subject.objects.all()
        Course_B_subject_list = models.Course_B_subject.objects.all()
        Course_C_subject_list = models.Course_C_subject.objects.all()
        System_common_list = models.System_common_subject.objects.all()
        System_subject_list = models.System_subject.objects.all()
        General_foreign_list = models.General_foreignlang_subject.objects.all()
        General_local_list = models.General_local_subject.objects.all()
        General_human_list = models.General_human_subject.objects.all()

        #合計単位数
        Course_A_Credits = 0
        Course_B_Credits = 0
        Course_C_Credits = 0
        System_common_Credits = 0
        System_Credits = 0
        General_foreign_Credits = 0
        General_local_Credits = 0
        General_human_Credits = 0

        for mygrade in My_Grade_list:
            for courseAsubject in Course_A_subject_list:
                if mygrade.subject_code == courseAsubject.subject_code:
                    Course_A_Credits += mygrade.pass_or_fail * courseAsubject.credit
            for courseBsubject in Course_B_subject_list:
                if mygrade.subject_code == courseBsubject.subject_code:
                    Course_B_Credits += mygrade.pass_or_fail * courseBsubject.credit
            for courseCsubject in Course_C_subject_list:
                if mygrade.subject_code == courseCsubject.subject_code:
                    Course_C_Credits += mygrade.pass_or_fail * courseCsubject.credit

            for systemcommonsubject in System_common_list:
                if mygrade.subject_code == systemcommonsubject.subject_code:
                    System_common_Credits += mygrade.pass_or_fail * systemcommonsubject.credit
            for systemsubject in System_subject_list:
                if mygrade.subject_code == systemsubject.subject_code:
                    System_Credits += mygrade.pass_or_fail * systemsubject.credit

            for general_foreign_subject in General_foreign_list:
                if mygrade.subject_code == general_foreign_subject.subject_code:
                    General_foreign_Credits += mygrade.pass_or_fail * general_foreign_subject.credit
            for general_local_subject in General_local_list:
                if mygrade.subject_code == general_local_subject.subject_code:
                    General_local_Credits += mygrade.pass_or_fail * general_local_subject.credit
            for general_human_subject in General_human_list:
                if mygrade.subject_code == general_human_subject.subject_code:
                    General_human_Credits += mygrade.pass_or_fail * general_human_subject.credit

        General_Credits = General_foreign_Credits + General_local_Credits + General_human_Credits

        option = {
            'credits_CourseA':Course_A_Credits,
            'credits_CourseB':Course_B_Credits,
            'credits_CourseC':Course_C_Credits,
            'credits_System':System_Credits,
            'credits_System_common':System_common_Credits,
            'credits_General':General_Credits,
            'credits_General_foreign':General_foreign_Credits,
            'credits_General_local':General_local_Credits,
            'credits_General_human':General_human_Credits,
        }

        return render(request, 'proffesional/result.html',option)

    else:
        error_message.append("csvがアップロードされていません")

        option = {
            'error_message':error_message
        }

        return render(request, 'proffesional/main.html',option)

    template_file = "proffesional/main.html"

    option = {

    }
    return render(request, template_file, option)




#コース科目登録用
def develop_courseA(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルCourse_A_subjectにデータを追加
        for line in csv_file:
            Course_A_subject, created =models.Course_A_subject.objects.get_or_create(subject_code=line[2])
            Course_A_subject.subject_code = line[2]
            Course_A_subject.subject_name = line[3]
            Course_A_subject.credit = line[1]
            Course_A_subject.compulsory_or_elective = line[0]
            Course_A_subject.save()

        return render(request, 'proffesional/developA.html')

    else:
        return render(request, 'proffesional/developA.html')

def develop_courseB(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルCourse_A_subjectにデータを追加
        for line in csv_file:
            Course_B_subject, created =models.Course_B_subject.objects.get_or_create(subject_code=line[2])
            Course_B_subject.subject_code = line[2]
            Course_B_subject.subject_name = line[3]
            Course_B_subject.credit = line[1]
            Course_B_subject.compulsory_or_elective = line[0]
            Course_B_subject.save()

        return render(request, 'proffesional/developB.html')

    else:
        return render(request, 'proffesional/developB.html')

def develop_courseC(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルCourse_A_subjectにデータを追加
        for line in csv_file:
            Course_C_subject, created =models.Course_C_subject.objects.get_or_create(subject_code=line[2])
            Course_C_subject.subject_code = line[2]
            Course_C_subject.subject_name = line[3]
            Course_C_subject.credit = line[1]
            Course_C_subject.compulsory_or_elective = line[0]
            Course_C_subject.save()

        return render(request, 'proffesional/developC.html')

    else:
        return render(request, 'proffesional/developC.html')


#学部・学科共通科目登録用
def develop_system_common(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルSystem_subjectにデータを追加
        for line in csv_file:
            System_common_subject, created =models.System_common_subject.objects.get_or_create(subject_code=line[1])
            System_common_subject.subject_code = line[1]
            System_common_subject.subject_name = line[2]
            System_common_subject.credit = line[0]
            #System_common_subject.compulsory_or_elective = line[0]
            System_common_subject.save()

        return render(request, 'proffesional/develop_system_common.html')

    else:
        return render(request, 'proffesional/develop_system_common.html')

def develop_system(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルSystem_subjectにデータを追加
        for line in csv_file:
            System_subject, created =models.System_subject.objects.get_or_create(subject_code=line[1])
            System_subject.subject_code = line[1]
            System_subject.subject_name = line[2]
            System_subject.credit = line[0]
            #System_subject.compulsory_or_elective = line[0]
            System_subject.save()

        return render(request, 'proffesional/develop_system.html')

    else:
        return render(request, 'proffesional/develop_system.html')


#一般教養科目登録用
def develop_general_foreignlang(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルGeneral_subjectにデータを追加
        for line in csv_file:
            General_foreignlang_subject, created =models.General_foreignlang_subject.objects.get_or_create(subject_code=line[2])
            General_foreignlang_subject.subject_code = line[2]
            General_foreignlang_subject.subject_name = line[3]
            General_foreignlang_subject.credit = line[1]
            General_foreignlang_subject.compulsory_or_elective = line[0]
            General_foreignlang_subject.save()

        return render(request, 'proffesional/develop_general_foreignlang.html')

    else:
        return render(request, 'proffesional/develop_general_foreignlang.html')

def develop_general_human(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルGeneral_subjectにデータを追加
        for line in csv_file:
            General_human_subject, created =models.General_human_subject.objects.get_or_create(subject_code=line[2])
            General_human_subject.subject_code = line[2]
            General_human_subject.subject_name = line[3]
            General_human_subject.credit = line[1]
            General_human_subject.compulsory_or_elective = line[0]
            General_human_subject.save()

        return render(request, 'proffesional/develop_general_human.html')

    else:
        return render(request, 'proffesional/develop_general_human.html')

def develop_general_local(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルGeneral_subjectにデータを追加
        for line in csv_file:
            General_local_subject, created =models.General_local_subject.objects.get_or_create(subject_code=line[2])
            General_local_subject.subject_code = line[2]
            General_local_subject.subject_name = line[3]
            General_local_subject.credit = line[1]
            General_local_subject.compulsory_or_elective = line[0]
            General_local_subject.save()

        return render(request, 'proffesional/develop_general_local.html')

    else:
        return render(request, 'proffesional/develop_general_local.html')

