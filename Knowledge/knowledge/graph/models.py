from django.db import models

# Create your models here.

class Node(models.Model):
    N_id =models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='名称')
    belong_to = models.CharField(max_length=50, verbose_name='结点归类')
    desc = models.CharField(max_length=50, verbose_name='描述')
    category = models.IntegerField(max_length=50, verbose_name='结点类别')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')


class Edge(models.Model):
    E_id= models.IntegerField(primary_key=True)
    source = models.CharField(max_length=50, verbose_name='源点')
    target = models.CharField(max_length=50, verbose_name='终点')
    value = models.CharField(max_length=50, verbose_name='关系名称')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
