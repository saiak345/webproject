from django.contrib import admin

from college.models import student

# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['id','name','fname','classname','contact']

admin.site.register(student,studentadmin)
