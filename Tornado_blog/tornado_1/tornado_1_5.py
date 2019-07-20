# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 00:15
# @Author  : Bryce Liu
# @FileName: tornado_1_5.py.py

# conding:utf-8
import os

# Redis配置
redis_options = {
    'redis_host': '127.0.0.1',
    'redis_port': 6379,
    'redis_pass': '',
}

# Tornado app配置
settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'static_path': os.path.join(os.path.dirname(__file__), 'statics'),
    'cookie_secret': 'QJ76Hbd+N80XhKS7HCKskOUE2snIH06SHxXlG=',
    'xsrf_cookies': False,
    'login_url': '/login',
    'debug': True,
}

# 日志
log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
