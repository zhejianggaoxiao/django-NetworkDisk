import os
from datetime  import  datetime


from django.db import models

class FileModel(models.Model):
    fname = models.CharField(max_length=100,verbose_name="文件名")
    file = models.FileField(max_length=100,upload_to="up_file/%Y/%m/", verbose_name="文件")
    owner = models.CharField(max_length=20, verbose_name="上传用户", default="admin")

    # add_time = models.DateTimeField(default=datetime.now)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "上传文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.fname

    # 重载对象的delete方法，从而将文件一并删除
    def delete(self, *args,**kwargs):
        if os.path.isfile(self.file.path):
            os.remove(self.file.path)
        super(FileModel, self).delete(*args, **kwargs)
