from django.test import TestCase
from .models import Node, Edge

# Create your tests here.
def create_data():
    data = [
        {'name': '铀资源地质学', 'value': {'belong_to': '地质类', 'desc': '这是一本地质类的书', }, 'category': 0, 'draggable': True},
        {'name': '第一章', 'value': {'belong_to': '矿床', 'desc': '描述矿床', }, 'category': 1, 'draggable': True},
        {'name': '第二章', 'value': {'belong_to': '矿石', 'desc': '描述矿石', }, 'category': 1, 'draggable': True},
    ]

    links = [
        {'source': '地质分析', 'target': '第一章', 'category': 0, 'value': '包含', 'symbolSize': 10, },
        {'source': '地质分析', 'target': '第二章', 'category': 0, 'value': '包含', 'symbolSize': 10, },
    ]
    return data, links