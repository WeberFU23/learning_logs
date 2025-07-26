from django.contrib import admin

# Register your models here.

from .models import Topic,Entry

admin.site.register(Topic)#允许通过网站管理模型
admin.site.register(Entry)