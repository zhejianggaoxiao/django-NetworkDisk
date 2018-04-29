"""
-------------------------------------------------
   File Name：     forms.py
   Description :
   Author :       gaox
   date：          4/28/18
-------------------------------------------------
   Change Activity:
                   4/28/18:
-------------------------------------------------
"""
__author__ = 'gaox'


from .models import FileModel
from django import forms

# 采用模型表单
class FileModelForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['fname','file','owner']

# # 采用普通表单
# class FileModelForm(forms.Form):
#     fname = forms.CharField(max_length=100)
#     file = forms.FileField()
