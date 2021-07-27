from django.contrib import admin
from .models import students,staffs,attendance,feedback,exam,extenduser
# Register your models here.
admin.site.register(students)
admin.site.register(staffs)
admin.site.register(attendance)
admin.site.register(feedback)
admin.site.register(exam)
admin.site.register(extenduser)
