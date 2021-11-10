from django.urls import path
from . import views

app_name = 'proffesional'

urlpatterns = [
    #メイン画面
    path('',views.mainView, name = 'main'),
    #単位取得状況表示画面
    path('result',views.result, name = 'result'),
    #CSVアップロードテスト用
    path('csv_test',views.csv_test, name = 'csv_test'),
]