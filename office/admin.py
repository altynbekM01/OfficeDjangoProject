from django.contrib import admin


from office.models import Employee
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','surname', 'middleName', 'position', 'joined_at', 'salary', 'chief']
    list_filter = ['name','surname', 'middleName', 'joined_at', 'position', 'salary']
    list_editable = ['chief']



admin.site.register(Employee, EmployeeAdmin)

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass




