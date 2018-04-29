"""
-------------------------------------------------
   File Name：     urls.py
   Description :
   Author :       gaox
   date：          4/28/18
-------------------------------------------------
   Change Activity:
                   4/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'


from django.urls import path, include
from .views import IndexView, SaveFileView, DeleteFileView, SignupView
# 注册实现
import django.contrib.auth.views as authview

app_name="myCloud"

urlpatterns = [
    path('',IndexView.as_view(), name="index"),
    path('save_file/',SaveFileView.as_view(), name="savefile"),
    path('del_file/<int:id>/', DeleteFileView.as_view(), name="delfile"),

    path('login/', authview.login, name="login"),
    path('logout/', authview.logout, name="logout"),
    path('signup/',SignupView.as_view(), name="signup" ),



]