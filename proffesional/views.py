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

        return render(request, 'proffesional/main.html')

    else:
        return render(request, 'proffesional/main.html')

    template_file = "proffesional/main.html"

    option = {

    }
    return render(request, template_file, option)

def develop(request):
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
