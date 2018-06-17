from django.contrib import admin
from gecko import models

# Register your models here.

class SAadmin(admin.ModelAdmin):
     list_display = ('name','department','qq','position','date')
     list_editable = ('department',)
     list_filter = ('position',)
     search_fields = ('qq', 'name')
     raw_id_fields = ('consult_course',)
     filter_horizontal = ('tags',)

#admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Administrators, SAadmin)
admin.site.register(models.Tag)
admin.site.register(models.Course)





