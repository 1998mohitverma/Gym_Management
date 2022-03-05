from django.contrib import admin
from .models import Enquiry, Equipment, Plan, Member
# Register your models here.

admin.site.register(Enquiry)
admin.site.register(Equipment)
admin.site.register(Plan)

@admin.register(Member)
class Member_admin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','age','gender','plan','photo','joindate','expiredate','initialamount']
    