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
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='ansi')
        csv_file = csv.reader(form_data)
        # csvからモデルMy_Gradesにデータを追加
        for line in csv_file:
            my_grades, created =models.My_Grades.objects.get_or_create(subject_name=line[4])
            my_grades.subject_name = line[4]
            my_grades.subject_code = line[3]
            if line[7] == "合":
                my_grades.pass_or_fail = 1
            else:
                my_grades.pass_or_fail = 0
            my_grades.save()

        #自分の成績をリストに格納
        My_Grade_list = models.My_Grades.objects.all()
        #単位数データをリストに格納
        Course_subject_list = models.Course_subject.objects.all()
        System_subject_list = models.System_subject.objects.all()
        General_subject_list = models.General_subject.objects.all()

        #合計単位数
        Course_Credits = 0
        System_Credits = 0
        General_Credits = 0

        for mygrade in My_Grade_list:
            for coursesubject in Course_subject_list:
                if mygrade.subject_code == coursesubject.subject_code:
                    Course_Credits += mygrade.pass_or_fail * coursesubject.credit
            for systemsubject in System_subject_list:
                if mygrade.subject_code == systemsubject.subject_code:
                    System_Credits += mygrade.pass_or_fail * systemsubject.credit
            for generalsubject in General_subject_list:
                if mygrade.subject_code == generalsubject.subject_code:
                    General_Credits += mygrade.pass_or_fail * generalsubject.credit

        option = {
            'credits_Course':Course_Credits,
            'credits_System':System_Credits,
            'credits_General':General_Credits,
        }

        return render(request, 'proffesional/result.html',option)

    else:
        return render(request, 'proffesional/main.html')

    template_file = "proffesional/main.html"

    option = {

    }
    return render(request, template_file, option)

def develop_course(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='ansi')
        csv_file = csv.reader(form_data)
        # csvからモデルCourse_subjectにデータを追加
        for line in csv_file:
            Course_subject, created =models.Course_subject.objects.get_or_create(subject_code=line[2])
            Course_subject.subject_code = line[2]
            Course_subject.credit = line[1]
            Course_subject.compulsory_or_elective = line[0]
            Course_subject.save()

        return render(request, 'proffesional/develop.html')

    else:
        return render(request, 'proffesional/develop.html')

    template_file = "proffesional/main.html"

    option = {

    }
    return render(request, template_file, option)

def develop_system(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='ansi')
        csv_file = csv.reader(form_data)
        # csvからモデルSystem_subjectにデータを追加
        for line in csv_file:
            System_subject, created =models.System_subject.objects.get_or_create(subject_code=line[1])
            System_subject.subject_code = line[1]
            System_subject.credit = line[0]
            #System_subject.compulsory_or_elective = line[0]
            System_subject.save()

        return render(request, 'proffesional/develop_system.html')

    else:
        return render(request, 'proffesional/develop_system.html')

    template_file = "proffesional/main.html"

    option = {

    }
    return render(request, template_file, option)

def develop_general(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='ansi')
        csv_file = csv.reader(form_data)
        # csvからモデルGeneral_subjectにデータを追加
        for line in csv_file:
            General_subject, created =models.General_subject.objects.get_or_create(subject_code=line[2])
            General_subject.subject_code = line[2]
            General_subject.credit = line[1]
            General_subject.compulsory_or_elective = line[0]
            General_subject.save()

        return render(request, 'proffesional/develop_general.html')

    else:
        return render(request, 'proffesional/develop_general.html')

    template_file = "proffesional/main.html"

    option = {

    }
    return render(request, template_file, option)
