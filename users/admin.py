from django.contrib import admin
from .models import User, Sections, Intakes, Departments, Student, Teacher, Profile

admin.site.register(User)
admin.site.register(Intakes)
admin.site.register(Sections)
admin.site.register(Departments)
admin.site.register(Teacher)
admin.site.register(Profile)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'intake', 'section', 'department', 'shift', 'is_class_cr')
    search_fields = ('name', 'intake__name', 'section__name', 'department__name')
    list_filter = ('intake', 'section', 'department', 'shift')  # Optional filtering

    # Optionally customize field ordering
    # ordering = ('intake', 'department', 'section', 'name')

admin.site.register(Student, StudentAdmin)