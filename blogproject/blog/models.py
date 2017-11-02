# coding:utf-8
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#分类
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100) #姓名
    def __str__(self):
        return self.name

#标签
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100) #姓名
    def __str__(self):
        return self.name

#文章
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70) #文章标题
    body = models.TextField() #文章正文    
    created_time = models.DateTimeField() #文章创建时间
    modified_time = models.DateTimeField() #文章最后一次修改时间
    excerpt = models.CharField(max_length=200, blank=True) #文章摘要 设置blank=True允许空值
    category = models.ForeignKey(Category) #分类 和文章一对多对应关系
    tags = models.ManyToManyField(Tag, blank=True) #标签 和文章多对对对应关系 允许空值
    author = models.ForeignKey(User) #作者 User是从django.contrib.auth.models导入  
    created_time = models.DateTimeField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
