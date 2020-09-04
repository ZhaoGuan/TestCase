#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('test', views.test, name='test'),
    path('get_attributes', views.get_attributes, name='get_attributes'),
    path('add_attribute', views.add_attribute, name='add_attribute'),
    path('del_attributes', views.del_attributes, name='del_attributes'),
    path('create_element', views.create_element, name='create_element'),
    path('get_elements_info', views.get_elements_info, name='get_elements_info'),
    path('del_element', views.del_element, name='del_element'),
    path('recording', views.recording, name='recording'),
]
