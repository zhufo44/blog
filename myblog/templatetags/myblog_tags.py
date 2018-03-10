from ..models import Post,Category,Tag
from django import template
from django.db.models import Count
#自定义模板标签
register = template.Library()

@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all().order_by('-create_time')[:num]
#使用register将普通的Python函数变成Django的模板标签

@register.simple_tag
def archives():
    return Post.objects.dates('create_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)



