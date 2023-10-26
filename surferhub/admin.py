from django.contrib import admin

# Importing models
from .models import CustomUser, UserProfile


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    search_fields = ('username', 'email',)
    list_filter = ('is_staff', 'is_active',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country')
    search_fields = ('user__username', 'country')
    list_filter = ('country',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)