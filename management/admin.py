#coding:utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from management.models import *


class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (MyUserInline,)
    list_per_page = 10
    list_display = ['id', 'username', 'password', 'email', 'is_staff']


class ImgAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name', 'description', 'img', 'book']


class MyUserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['user', 'uid', 'nickname', 'permission', 'user_state']


class ClubAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name', 'price', 'author', 'publish_date', 'category', 'detail']


class club_zixunAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['aid', 'activity_name', 'activity_describe', 'activity_person', 'activity_img']


class MyadminAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['username', 'password', 'name', 'email']


admin.site.site_header = '社团后台管理'
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Img, ImgAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(club_zixun, club_zixunAdmin)
admin.site.register(Myadmin, MyadminAdmin)

