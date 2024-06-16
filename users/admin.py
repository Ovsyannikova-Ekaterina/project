#   users/admin.py


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Parent, Student, Teacher
from .forms import CustomUserCreationForm, CustomUserChangeForm, StudentForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'is_staff', 'is_active']
    list_filter = ['user_type', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('first_name', 'last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ['email', 'username']
    ordering = ['email']

class ParentAdmin(admin.ModelAdmin):
    list_display = ['user_username', 'phone', 'email', 'relation_to_child']

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = 'Username'

class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    list_display = ['user_username', 'birth_date', 'parent_username']

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = 'Username'

    def parent_username(self, obj):
        return obj.parent.user.get_full_name()

    parent_username.short_description = 'Parent Username'

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user_username', 'position', 'phone', 'email']

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = 'Username'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
