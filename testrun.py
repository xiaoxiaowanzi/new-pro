# -*- coding: utf-8 -*-
'''
时间：2017-11-28
作者：小丸子
标题：配置文件
描述：采用的是字典方式来管理配置文件
'''
from config import Deploymentconfig  
import config
filehome = Deploymentconfig["filehome"]
print(filehome)
username = config.Testconfig["username"]
print(username)
