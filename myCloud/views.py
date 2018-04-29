from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View


from .forms import FileModelForm
from .models import FileModel
from .tables import FileTable

from .utils.loginrequired import LoginRequiredMixin
# Create your views here.
class IndexView(LoginRequiredMixin,View):

    def get(self,request):
        all_file = FileModel.objects.all()
        context = {'table':''}
        if all_file:
            table = FileTable(all_file)
            context = {"table": table}
        return render(request, "myCloud/index.html", context)



# # 采用普通表单方式
# class SaveFileView(View):
#     def post(self,request):
#         data = FileModelForm(request.POST, request.FILES)
#         if data.is_valid():
#             form = FileModel()
#             form.fname = data.cleaned_data["fname"]
#             form.file = data.cleaned_data['file']
#             form.save()
#             return HttpResponse("上传成功")
#         else:
#             return HttpResponse("上传失败")

# 采用模型表单方式

class SaveFileView(View):
    def post(self,request):
        form = FileModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("myCloud:index"))
        else:
            return HttpResponse("上传失败")

class DeleteFileView(View):
    def get(self,request,id):
        del_file = FileModel.objects.filter(id=id)
        if del_file:
            del_file[0].delete()
            return HttpResponseRedirect(reverse("myCloud:index"))
        else:
            return HttpResponse("文件不存在或已删除")











