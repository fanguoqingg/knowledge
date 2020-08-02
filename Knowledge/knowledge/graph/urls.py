from django.urls import path
from . import views

# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/29 22:04
@Auth ： guoqing Fan
@File ：urls.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
urlpatterns = [
    path('', views.graph, name='index'),
    # path('add/', views.add, name='delete'),
    path('delete/', views.delete, name='delete'),
]