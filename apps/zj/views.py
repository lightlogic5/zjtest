# _*_ encoding:utf-8 _*_
from django.shortcuts import render

# 引入同一目录下的模型中的类

from .models import zj

# Create your views here.
# 获取所有填写的总结
def getform(request):
    all_messages = zj.objects.all()
    # all_messages = zj.objects.filter( employ_name = "",title_id = "")
    for message in all_messages:
        print message.title
    return render(request,'get_message.html')
# 填写总结,获取的值与form的name一一对应
def sub_form(request):
    # 实例化1个zj模型的对象
    em_zj = zj()
    # 首先判断是否是post因为直接输入地址是get容易出错
    # 此处打断点调试，鼠标放在request处，可以看到method属性是get,step over f6单步调试，需要输入数据进入post后进行
    # F8跳到下1个断点，都需要在页面执行操作才可进行下一步
    # get是python中取字典中数据的方法，如果取不到就为默认值空
    if request.method == 'POST':
        employ_name = request.POST.get('name','')
        title = request.POST.get('title', '')
        content = request.POST.get('message', '')
        em_zj.employ_name = employ_name
        em_zj.title = title
        em_zj.content = content
        em_zj.save()
    return render(request, 'message_form.html')