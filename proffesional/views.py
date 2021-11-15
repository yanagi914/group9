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

def csv_test(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='ansi')
        csv_file = csv.reader(form_data)
        # csvからモデルMy_Gradesにデータを追加
        for line in csv_file:
            my_grades, created =models.My_Grades.objects.get_or_create(subject_name=line[4])
            my_grades.subject_name = line[4]
            my_grades.subject_code = line[3]
            my_grades.pass_or_fail = line[7]
            my_grades.save()

        return render(request, 'proffesional/csv_test.html')

    else:
        return render(request, 'proffesional/csv_test.html')

    template_file = "proffesional/csv_test.html"

    option = {

    }
    return render(request, template_file, option)
