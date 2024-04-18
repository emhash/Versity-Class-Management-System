from django.contrib import admin
from .models import UpcomingExams,ClassRoutine,Assignments,Announcements

admin.site.register(UpcomingExams)
admin.site.register(ClassRoutine)
admin.site.register(Assignments)
admin.site.register(Announcements)
