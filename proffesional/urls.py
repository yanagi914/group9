from django.urls import path
from . import views

app_name = 'proffesional'

urlpatterns = [
    #タイトル画面
    path('',views.title, name = 'title'),
    #単位取得状況表示画面
    path('result',views.result, name = 'result'),
    #main用(ただし、使うことはない)
    path('main',views.main, name = 'main'),
    #コース科目登録用
    path('develop_courseA',views.develop_courseA, name = 'develop_courseA'),
    #コース科目登録用
    path('develop_courseB',views.develop_courseB, name = 'develop_courseB'),
    #コース科目登録用
    path('develop_courseC',views.develop_courseC, name = 'develop_courseC'),
    #コース科目登録用
    path('develop_system_common',views.develop_system_common, name = 'develop_system_common'),
    #コース科目登録用
    path('develop_system',views.develop_system, name = 'develop_system'),
    #コース科目登録用
    path('develop_general_foreignlang',views.develop_general_foreignlang, name = 'develop_general_foreignlang'),
    #コース科目登録用
    path('develop_general_human',views.develop_general_human, name = 'develop_general_human'),
    #コース科目登録用
    path('develop_general_local',views.develop_general_local, name = 'develop_general_local'),
    #コース科目登録用 サブ
    path('develop_system_sub',views.develop_system_sub, name = 'develop_system_sub'),
    #コース科目登録用
    path('develop_system_common_sub',views.develop_system_common_sub, name = 'develop_system_common_sub'),
    #コース科目登録用
    path('develop_general_foreignlang_sub',views.develop_general_foreignlang_sub, name = 'develop_general_foreignlang_sub'),
    #コース科目登録用
    path('develop_general_human_sub',views.develop_general_human_sub, name = 'develop_general_human_sub'),
    #コース科目登録用
    path('develop_general_local_sub',views.develop_general_local_sub, name = 'develop_general_local_sub'),
    #登録用ページ
    path('develop', views.develop, name= 'develop')
]