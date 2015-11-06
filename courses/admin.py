from django.contrib import admin
from .models import *
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'dept')
	search_fields = ['name']

class ProfAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'dept')


admin.site.register(Course, CourseAdmin)
admin.site.register(Prof, ProfAdmin)
admin.site.register(Dept)
admin.site.register(Term)
admin.site.register(Period)
admin.site.register(Distrib)
admin.site.register(WC)