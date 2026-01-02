from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import User

# Register your models here.


class UserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name',
                    'last_name', 'is_active']
    list_filter = ['is_active', 'is_staff']

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'date_of_birth'
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.is_active = False

        super().save_model(request, obj, form, change)

        if obj.pk is None:
            self.message_user(
                request,
                "User created successfully!",
                level='SUCCESS'
            )


admin.site.register(User, UserAdmin)
