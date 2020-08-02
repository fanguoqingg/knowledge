from django.contrib import admin
from .models import Edge, Node

# Register your models here.

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'belong_to', 'desc', 'category')


@admin.register(Edge)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('source', 'target', 'value')