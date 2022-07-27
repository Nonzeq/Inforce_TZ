from django.contrib import admin

from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'username', )
    list_display_links = ('id', 'username')
    search_fields = ('username',)
    
admin.site.register(Employee, EmployeeAdmin)
