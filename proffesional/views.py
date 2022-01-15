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

    if 'choice_output' in request.POST:
        output = request.POST.get('choice_output', None)
    else:
        output = ""

    if 'csv' in request.FILES:

        # csvを取り込む
        models.My_Grades.objects.all().delete() #My_Gradesをまず初期化
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='ansi')
        csv_file = csv.reader(form_data)

        csv_list = [row for row in csv_file]

        #CSVの形式を判定
        if csv_list[4][1] == "開講年度": #SIRS~(学外からダウンロードしたやつ？)
            mode = "SIRS"
        elif csv_list[4][1] == "科目大区分": #KakuteiseisekiCsv(airmitからダウンロードしたやつ？)
            mode = "kakuteiseiseki"
        else:
            error_message.append("csvの形式が正しくありません")
        
        # csvからモデルMy_Gradesにデータを追加
        for index,line in enumerate(csv_list):

            #最初の氏名とかラベルとかをスキップ
            if index < 4:
                continue

            #csv -> My_Gradesにデータを読み込み
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
            #自分の成績をリストに格納
            My_Grade_list = models.My_Grades.objects.all()
            #単位数データをリストに格納
            Course_A_subject_list = models.Course_A_subject.objects.all()
            Course_A_subject_list2 = []
            Course_B_subject_list = models.Course_B_subject.objects.all()
            Course_B_subject_list2 = []
            Course_C_subject_list = models.Course_C_subject.objects.all()
            Course_C_subject_list2 = []
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

            #取っていない科目を表示させるところ
            for courseAsubject in Course_A_subject_list:
                Course_A_subject_list2.append(courseAsubject.subject_name)
            for courseBsubject in Course_B_subject_list:
                Course_B_subject_list2.append(courseBsubject.subject_name)
            for courseCsubject in Course_C_subject_list:
                Course_C_subject_list2.append(courseCsubject.subject_name)

            #照合処理・単位計算
            for mygrade in My_Grade_list:
                for courseAsubject in Course_A_subject_list:
                    if mygrade.subject_code == courseAsubject.subject_code:
                        Course_A_Credits += mygrade.pass_or_fail * courseAsubject.credit
                        Course_A_subject_list2.remove(courseAsubject.subject_name)
                for courseBsubject in Course_B_subject_list:
                    if mygrade.subject_code == courseBsubject.subject_code:
                        Course_B_Credits += mygrade.pass_or_fail * courseBsubject.credit
                        Course_B_subject_list2.remove(courseBsubject.subject_name)
                for courseCsubject in Course_C_subject_list:
                    if mygrade.subject_code == courseCsubject.subject_code:
                        Course_C_Credits += mygrade.pass_or_fail * courseCsubject.credit
                        Course_C_subject_list2.remove(courseCsubject.subject_name)

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
                'mode':mode,
                'error_message':error_message,
                'output':output,
                'Course_A_subject_list2':Course_A_subject_list2,
                'Course_B_subject_list2':Course_B_subject_list2,
                'Course_C_subject_list2':Course_C_subject_list2,
            }
        elif mode == "kakuteiseiseki":
            #自分の成績をリストに格納
            My_Grade_list = models.My_Grades.objects.all()
            #単位数データをリストに格納
            Course_A_subject_list = models.Course_A_subject.objects.all()
            Course_A_subject_list2 = []
            Course_B_subject_list = models.Course_B_subject.objects.all()
            Course_B_subject_list2 = []
            Course_C_subject_list = models.Course_C_subject.objects.all()
            Course_C_subject_list2 = []
            System_common_list = models.System_common_subject.objects.all()
            System_subject_list = models.System_subject.objects.all()
            General_foreign_list = models.General_foreignlang_subject.objects.all()
            General_local_list = models.General_local_subject.objects.all()
            General_human_list = models.General_human_subject.objects.all()
            System_common_list_sub = models.System_common_subject_sub.objects.all()
            System_common_list_sub2 = []
            System_subject_list_sub = models.System_subject_sub.objects.all()
            System_subject_list_sub2 = []
            General_foreign_list_sub = models.General_foreignlang_subject_sub.objects.all()
            General_foreign_list_sub2 = []
            General_local_list_sub = models.General_local_subject_sub.objects.all()
            General_local_list_sub2 = []
            General_human_list_sub = models.General_human_subject_sub.objects.all()
            General_human_list_sub2 = []

            #合計単位数
            Course_A_Credits = 0
            Course_B_Credits = 0
            Course_C_Credits = 0
            System_common_Credits = 0
            System_Credits = 0
            General_foreign_Credits = 0
            General_local_Credits = 0
            General_human_Credits = 0
            tmp_list = []

            #取っていない科目を表示させるところ
            for courseAsubject in Course_A_subject_list:
                Course_A_subject_list2.append(courseAsubject.subject_name)
            for courseBsubject in Course_B_subject_list:
                Course_B_subject_list2.append(courseBsubject.subject_name)
            for courseCsubject in Course_C_subject_list:
                Course_C_subject_list2.append(courseCsubject.subject_name)
            for systemCommonsubject in System_common_list_sub:
                System_common_list_sub2.append(systemCommonsubject.subject_name)
            for systemsubject in System_subject_list_sub:
                System_subject_list_sub2.append(systemsubject.subject_name)
            for generalforeignlang in General_foreign_list_sub:
                General_foreign_list_sub2.append(generalforeignlang.subject_name)
            for generalhuman in General_human_list_sub:
                General_human_list_sub2.append(generalhuman.subject_name)
            for generallocal in General_local_list_sub:
                General_local_list_sub2.append(generallocal.subject_name)

            #照合処理・単位計算
            for mygrade in My_Grade_list:
                for courseAsubject in Course_A_subject_list:
                    if (courseAsubject.subject_name.startswith(mygrade.subject_name)) and mygrade.isCheckedFlag == False: #srartswithは先頭一致を調べる関数
                        Course_A_Credits += mygrade.pass_or_fail * courseAsubject.credit
                        mygrade.isCheckedFlag = True
                        Course_A_subject_list2.remove(courseAsubject.subject_name)
                for courseBsubject in Course_B_subject_list:
                    if (courseBsubject.subject_name.startswith(mygrade.subject_name)) and mygrade.isCheckedFlag == False:
                        Course_B_Credits += mygrade.pass_or_fail * courseBsubject.credit
                        mygrade.isCheckedFlag = True
                        Course_B_subject_list2.remove(courseBsubject.subject_name)
                for courseCsubject in Course_C_subject_list:
                    if (courseCsubject.subject_name.startswith(mygrade.subject_name)) and mygrade.isCheckedFlag == False:
                        Course_C_Credits += mygrade.pass_or_fail * courseCsubject.credit
                        mygrade.isCheckedFlag = True
                        Course_C_subject_list2.remove(courseCsubject.subject_name)

                for systemcommonsubject in System_common_list:
                    if (systemcommonsubject.subject_name.startswith(mygrade.subject_name)) and mygrade.isCheckedFlag == False:
                        System_common_Credits += mygrade.pass_or_fail * systemcommonsubject.credit
                        mygrade.isCheckedFlag = True
                        for scs in System_common_list_sub2:
                            if (systemcommonsubject.subject_name.startswith(scs)):
                                System_common_list_sub2.remove(scs)
                for systemsubject in System_subject_list:
                    if (systemsubject.subject_name.startswith(mygrade.subject_name)) and mygrade.isCheckedFlag == False:
                        System_Credits += mygrade.pass_or_fail * systemsubject.credit
                        mygrade.isCheckedFlag = True
                        for sss in System_subject_list_sub2:
                            if (systemsubject.subject_name.startswith(sss)):
                                System_subject_list_sub2.remove(sss)

                for general_foreign_subject in General_foreign_list:
                    if (general_foreign_subject.subject_name.startswith(mygrade.subject_name)) and mygrade.isCheckedFlag == False:
                        General_foreign_Credits += mygrade.pass_or_fail * general_foreign_subject.credit
                        mygrade.isCheckedFlag = True
                        for gfs in General_foreign_list_sub2:
                            if (general_foreign_subject.subject_name.startswith(gfs)):
                                General_foreign_list_sub2.remove(gfs)
                for general_local_subject in General_local_list:
                    if (general_local_subject.subject_name.startswith(mygrade.subject_name)) and mygrade.isCheckedFlag == False:
                        General_local_Credits += mygrade.pass_or_fail * general_local_subject.credit
                        mygrade.isCheckedFlag = True
                        for gls in General_local_list_sub2:
                            if (general_local_subject.subject_name.startswith(gls)):
                                General_local_list_sub2.remove(gls)
                for general_human_subject in General_human_list:
                    if (general_human_subject.subject_name.startswith(mygrade.subject_name)) and mygrade.isCheckedFlag == False:
                        General_human_Credits += mygrade.pass_or_fail * general_human_subject.credit
                        mygrade.isCheckedFlag = True
                        for ghs in General_human_list_sub2:
                            if (general_human_subject.subject_name.startswith(ghs)):
                                General_human_list_sub2.remove(ghs)

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
                'mode':mode,
                'tmp_list':tmp_list,
                'error_message':error_message,
                'output':output,
                'Course_A_subject_list2':Course_A_subject_list2,
                'Course_B_subject_list2':Course_B_subject_list2,
                'Course_C_subject_list2':Course_C_subject_list2,
                'System_subject_list_sub2':System_subject_list_sub2,
                'System_common_list_sub2':System_common_list_sub2,
                'General_foreign_list_sub2':General_foreign_list_sub2,
                'General_human_list_sub2':General_human_list_sub2,
                'General_local_list_sub2':General_local_list_sub2,


            }


        if output == "1": #卒業要件
            temp_dict = {

                'Course_A':19.0,
                'Course_B':8.0,
                'Course_C':25.0,
                'System_common':26.0,
                'System':27.0,
                'General':24.0,
                'General_foreign':9.0,
                'General_local':2.0,
                'General_human':13.0
            }

            option.update(temp_dict)

        elif output == "0": #卒業研究着手要件
            temp_dict = {

                'Course_A':11.0,
                'Course_B':4.0,
                'Course_C':15.0,
                'System_common':23.0,
                'System':25.0,
                'General':16.0,
                'General_foreign':7.0,
                'General_local':1.0,
                'General_human':8.0
            }

            option.update(temp_dict)
        
        else:
            error_message.append("どちらを判定するか選択してください")

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

#学部・学科共通科目登録用 サブ
def develop_system_common_sub(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルSystem_subjectにデータを追加
        for line in csv_file:
            System_common_subject, created =models.System_common_subject_sub.objects.get_or_create(subject_code=line[1])
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

def develop_system_sub(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルSystem_subjectにデータを追加
        for line in csv_file:
            System_subject, created =models.System_subject_sub.objects.get_or_create(subject_code=line[1])
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

#一般教養科目登録用 サブ
def develop_general_foreignlang_sub(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルGeneral_subjectにデータを追加
        for line in csv_file:
            General_foreignlang_subject, created =models.General_foreignlang_subject_sub.objects.get_or_create(subject_code=line[2])
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

def develop_general_human_sub(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルGeneral_subjectにデータを追加
        for line in csv_file:
            General_human_subject, created =models.General_human_subject_sub.objects.get_or_create(subject_code=line[2])
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

def develop_general_local_sub(request):
    if 'csv' in request.FILES:
        # csvを取り込む
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        # csvからモデルGeneral_subjectにデータを追加
        for line in csv_file:
            General_local_subject, created =models.General_local_subject_sub.objects.get_or_create(subject_code=line[2])
            General_local_subject.subject_code = line[2]
            General_local_subject.subject_name = line[3]
            General_local_subject.credit = line[1]
            General_local_subject.compulsory_or_elective = line[0]
            General_local_subject.save()

        return render(request, 'proffesional/develop_general_local.html')

    else:
        return render(request, 'proffesional/develop_general_local.html')

def develop(request):
    template_file = "proffesional/develop.html"

    option = {

    }
    return render(request, template_file, option)