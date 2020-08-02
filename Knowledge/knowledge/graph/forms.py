# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/2 10:22
@Auth ： guoqing Fan
@File ：forms.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

from django import forms
from .models import Node,Edge

class Nodefrom(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = Node
        # 定义表单包含的字段
        fields = ('N_id', 'name','belong_to','desc','category')

class Edgefrom(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = Edge
        # 定义表单包含的字段
        fields = ('E_id', 'source', 'target', 'value')
