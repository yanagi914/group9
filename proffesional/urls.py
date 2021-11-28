from django.urls import path
from . import views

app_name = 'proffesional'

urlpatterns = [
    #タイトル画面
    path('',views.title, name = 'title'),
    #単位取得状況表示画面
    path('result',views.result, name = 'result'),
    #開発用
    path('develop',views.develop, name = 'develop'),
    #main用(ただし、使うことはない)
    path('main',views.main, name = 'main'),
]