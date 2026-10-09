
from django.contrib import admin
from .models import Cource, Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')  # display data
    search_fields = ('name',)  # search based on feature
    list_filter = ('course',)  # filter


class CourceAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Cource, CourceAdmin)
admin.site.register(Student, StudentAdmin)
