import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Node, Edge
from .forms import Nodefrom
from .forms import Edgefrom

def get_data_links():
    data = Node.objects.all()
    node = []
    for d in data:
        da = {'value': {'belong_to': '', 'desc': '', }, 'category': 0}
        da['N_id']=d.N_id
        da['name'] = d.name
        da['value']['belong_to'] = d.belong_to
        da['value']['desc'] = d.desc
        da['category'] = int(d.category)
        node.append(da)

    links = Edge.objects.all()
    edge = []
    for l in links:
        li = {'source': '', 'target': '', 'category': 0, 'value': '', 'symbolSize': 10}
        li['source'] = l.source
        li['target'] = l.target
        li['value'] = l.value
        li['E_id'] = l.E_id
        edge.append(li)
    return node, edge
# Create your views here.

def graph(request):
    data, links = get_data_links()
    d1 = json.dumps(data)
    l1 = json.dumps(links)
    return render(request, 'graph/graph.html', {'data': d1, 'links': l1})

def delete(request): # 用来删除元素
    if request.method == 'GET':
        ID = request.GET.get('N_id')
        Node.objects.filter(name=ID).delete()
        Edge.objects.filter(source=ID).delete()
        Edge.objects.filter(target=ID).delete()
    return HttpResponse("删除成功!")
'''
def add(request):       #用来增加数据
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        Node_from = Nodefrom(request.POST,request.method)
        if Node_from.is_valid():
            new_N_id= Node_from.save(commit=False)
    return HttpResponse("添加成功")

def update(request):       #用来修改数据
    if request.method == 'GET':
        ID = request.GET.get('N_id')


       
    return HttpResponse("修改成功")

def find(request):       #用来查找数据
    if request.method == 'GET':
        pass
    return HttpResponse("")
'''

