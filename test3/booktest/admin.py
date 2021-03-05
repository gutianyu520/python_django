from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Test1)

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uname']
    pass


# admin.site.register(UserInfo, UserInfoAdmin)