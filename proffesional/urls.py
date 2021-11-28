from django.urls import path
from . import views

app_name = 'proffesional'

urlpatterns = [
    #タイトル画面
    path('',views.title, name = 'title'),
    #単位取得状況表示画面
    path('result',views.result, name = 'result'),
    #コース科目登録用
    path('develop_course',views.develop_course, name = 'develop_course'),
    #コース科目登録用
    path('develop_system',views.develop_system, name = 'develop_system'),
    #コース科目登録用
    path('develop_general',views.develop_general, name = 'develop_general'),
    #main用(ただし、使うことはない)
    path('main',views.main, name = 'main'),
]