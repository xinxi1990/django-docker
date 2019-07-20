#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
定义数据库字段
"""

from django.db import models
from django.utils import timezone
import datetime


class AndroidModels(models.Model):
    name = models.CharField(max_length=200,verbose_name='名称')
    age = models.IntegerField(default=0,verbose_name='年龄')

    class Meta:
        db_table = 't_android'  # 指明数据库表名

    def __unicode__(self):
        return u'%s %s' % (name, age)



