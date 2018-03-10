from django.contrib import admin
from  .models import Tag,Post,Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modify_time','category','author']


admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
# Register your models here.
