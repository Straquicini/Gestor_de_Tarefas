from django.contrib import admin
from .models import Employee, Task

# Employee Admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hourly_rate')
    ordering = ('name',)
    search_fields = ('name',)

# Task Admin
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'duration', 'completed', 'employee')
    ordering = ('-id',)
    list_filter = ('completed', 'employee')
    search_fields = ('task', 'description')