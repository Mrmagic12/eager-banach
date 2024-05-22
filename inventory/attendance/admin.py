from django.contrib import admin
from .models import Admin, Announcements, Attendance, Employee, Events, MobileScanUsers, StaticTime
# Register your models here.
admin.site.register(Admin)
admin.site.register(Announcements)
admin.site.register(Attendance)
admin.site.register(Employee)
admin.site.register(Events)
admin.site.register(MobileScanUsers)
admin.site.register(StaticTime)
