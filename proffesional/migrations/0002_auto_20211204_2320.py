# Generated by Django 3.2.3 on 2021-12-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proffesional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_A_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, verbose_name='科目名')),
                ('subject_code', models.CharField(max_length=10, verbose_name='授業コード')),
                ('credit', models.FloatField(default=0, verbose_name='単位数')),
                ('compulsory_or_elective', models.CharField(blank=True, max_length=100, verbose_name='必修・選択')),
            ],
        ),
        migrations.CreateModel(
            name='Course_B_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, verbose_name='科目名')),
                ('subject_code', models.CharField(max_length=10, verbose_name='授業コード')),
                ('credit', models.FloatField(default=0, verbose_name='単位数')),
                ('compulsory_or_elective', models.CharField(blank=True, max_length=100, verbose_name='必修・選択')),
            ],
        ),
        migrations.CreateModel(
            name='Course_C_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, verbose_name='科目名')),
                ('subject_code', models.CharField(max_length=10, verbose_name='授業コード')),
                ('credit', models.FloatField(default=0, verbose_name='単位数')),
                ('compulsory_or_elective', models.CharField(blank=True, max_length=100, verbose_name='必修・選択')),
            ],
        ),
        migrations.CreateModel(
            name='General_foreignlang_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, verbose_name='科目名')),
                ('subject_code', models.CharField(max_length=10, verbose_name='授業コード')),
                ('credit', models.FloatField(default=0, verbose_name='単位数')),
                ('compulsory_or_elective', models.CharField(blank=True, max_length=100, verbose_name='必修・選択')),
            ],
        ),
        migrations.CreateModel(
            name='General_human_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, verbose_name='科目名')),
                ('subject_code', models.CharField(max_length=10, verbose_name='授業コード')),
                ('credit', models.FloatField(default=0, verbose_name='単位数')),
                ('compulsory_or_elective', models.CharField(blank=True, max_length=100, verbose_name='必修・選択')),
            ],
        ),
        migrations.CreateModel(
            name='General_local_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, verbose_name='科目名')),
                ('subject_code', models.CharField(max_length=10, verbose_name='授業コード')),
                ('credit', models.FloatField(default=0, verbose_name='単位数')),
                ('compulsory_or_elective', models.CharField(blank=True, max_length=100, verbose_name='必修・選択')),
            ],
        ),
        migrations.CreateModel(
            name='System_common_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, verbose_name='科目名')),
                ('subject_code', models.CharField(max_length=10, verbose_name='授業コード')),
                ('credit', models.FloatField(default=0, verbose_name='単位数')),
                ('compulsory_or_elective', models.CharField(blank=True, max_length=100, verbose_name='必修・選択')),
            ],
        ),
        migrations.DeleteModel(
            name='Course_subject',
        ),
        migrations.DeleteModel(
            name='General_subject',
        ),
        migrations.AddField(
            model_name='my_grades',
            name='isCheckedFlag',
            field=models.BooleanField(default=False, verbose_name='チャック済みかの判定'),
        ),
    ]
