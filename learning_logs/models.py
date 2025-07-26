from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    #ModelBase 会根据它收集到的字段信息，动态地为你的 Topic 类生成一个 __init__ 方法（以及其他许多用于数据库交互的方法，如 save(), delete(), 查询集方法等）。
    #这个动态生成的 __init__ 方法知道所有定义的字段（例如 text, date_added），因此当你创建实例时，它可以正确地接受这些字段的值并将其赋给 self.text、self.date_added 等实例属性。
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='entries')#类属性：这行是在定义 Entry 类的时候，告诉 Django 这个类应该有什么样的字段，以及这些字段的类型和行为。这个定义是针对整个 Entry 类的，而不是针对某个特定的 Entry 实例。因此，这里不需要 self。
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."#实例属性：self.text 或 self.topic 是在操作一个 Entry 的具体实例时，用来访问该实例特有的 text 值或其关联的 topic 对象的。