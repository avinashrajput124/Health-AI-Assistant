from django.contrib import admin

from .models import UserProfile,AppleHealthStat

@admin.register(UserProfile)
class AppleHealthStatAdmin(admin.ModelAdmin):
    """
    Admin configuration for UserProfile model.
    """
    list_display = (
        'email', 'is_active','address')
    search_fields = ('user__username', 'email', 'is_active', 'phone_number')
    list_filter = ('email', 'phone_number', 'address')

@admin.register(AppleHealthStat)
class AppleHealthStatAdmin(admin.ModelAdmin):
    """
    Admin configuration for AppleHealthStat model.
    """
    list_display = (
        'user', 'dateOfBirth','created_at', 'updated_at'
    )
    search_fields = ('user__username', 'biologicalSex', 'activityMoveMode', 'HKWorkoutTypeIdentifier')
    list_filter = ('biologicalSex', 'activityMoveMode', 'created_at')
