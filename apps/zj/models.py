# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 点击models选择fileds可以看到django内置的数据类型
class zj(models.Model):
    # 数据库错误时，将除了init的所有文件都删除，并且删除数据库中的所有表
    # title_id = models.AutoField(max_length=50,primary_key=True, verbose_name=u"主键", default=1)
    employ_name = models.CharField(max_length=50, verbose_name=u"作者", default="")
    title = models.CharField(max_length=50, verbose_name=u"标题", default="")
    content = models.CharField(max_length=500, verbose_name=u"内容", default="")

    class Meta:
        verbose_name = "总结信息填报"
        verbose_name_plural = verbose_name
        # 指定数据表名和排序字段
        # db_table = "user_message"
        # ordering = "-title_id"

    def __unicode__(self):
        return self.title