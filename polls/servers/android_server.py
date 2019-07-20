#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
服务逻辑类
"""

from ..models.androidmodels import AndroidModels
import logging
logger = logging.getLogger('django')

class AnroidServer():


    def __init__(self):
        self.class_name = self.__class__.__name__


    def add_android(self,parames):
        '''
        添加
        :return:
        '''
        try:
            info  = AndroidModels(name=parames['name'], age=parames['age'])
            info.save()
            logger.info(self.class_name + str(info.id))
            result = {"code": "1","msg":"添加成功"}
        except Exception as e:
            logger.info(self.class_name + str(e))
            result = {"code": "10000","msg":"添加失败"}
        finally:
            logger.info(self.class_name + str(result))
            return result


    def update_android(self,parames):
        '''
        更新
        :return:
        '''
        try:
            info  = AndroidModels(name=parames['name'])
            info.age = parames['age']
            info.save()
            logger.info(self.class_name + str(info.id))
            result = {"code": "1","msg":"更新成功"}
        except Exception as e:
            logger.info(self.class_name + str(e))
            result = {"code": "10000","msg":"更新失败"}
        finally:
            logger.info(self.class_name + str(result))
            return result



    def del_android(self,parames):
        '''
        删除
        :return:
        '''
        try:
            info  = AndroidModels(id=parames['id'])
            info.delete()
            result = {"code": "1","msg":"删除成功"}
        except Exception as e:
            logger.info(self.class_name + str(e))
            result = {"code": "10000","msg":"删除失败"}
        finally:
            logger.info(self.class_name + str(result))
            return result