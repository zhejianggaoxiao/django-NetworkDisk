"""
-------------------------------------------------
   File Name：     tables.py
   Description :
   Author :        gaox
   date：          4/29/18
-------------------------------------------------
   Change Activity:
                   4/29/18:
-------------------------------------------------
"""
__author__ = 'gaox'

import django_tables2 as tables
from django_tables2.utils import A
from .models import FileModel


class FileTable(tables.Table):
    file = tables.columns.FileColumn(attrs={'a': {'download': ''}})
    file_delete = tables.LinkColumn('myCloud:delfile', args=[A('id')],text='删除',verbose_name='操作')
    class Meta:
        model = FileModel


