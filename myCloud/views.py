from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .forms import FileModelForm
from .models import FileModel
# Create your views here.
class IndexView(View):
    def get(self,request):
        context={}
        return render(request, 'myCloud/index.html', context)


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
            return HttpResponse("上传成功")
        else:
            return HttpResponse("上传失败")






