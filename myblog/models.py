#models.py 定义数据表，Django提供ORM（object retaliation mapping）支持
#通过 python mange.py makemigrations 和 python mange.py migrate 完成数据迁移
#可使用 python manage.py sqlmigrate myblog 0001
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
import markdown
from django.utils.html import strip_tags

class Category(models.Model):
    #每个类都要继承models.model,每一个类都对应一张数据表
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Tag(models.Model):
    #Django会自动创建ID
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create_time = models.DateField()
    modify_time = models.DateField()
    excerpt = models.CharField(max_length=100,blank=True)

    #关联数据表，存在一对多（Foreignkey）多对多（ManyToManyField）
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('myblog:detail',kwargs={'pk':self.pk})

    def save(self,*args,**kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save(*args,**kwargs)

    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])
    class Meta:
        ordering = ['-create_time']


# Create your models here.

