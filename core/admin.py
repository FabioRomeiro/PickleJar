from django.contrib import admin

from core.models import ActivityLog, Credential, User


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')


class CredentialAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'favorite', 'active', 'owner', 'last_updated')
    list_editable = ('active',)
    search_fields = ('name', 'username')
    readonly_fields = ('last_updated', 'last_accessed', 'created_at', 'owner', 'status', 'password')


class PassImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_url')
    search_fields = ('user',)


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'admin', 'passcoord']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',)}
         ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Credential, CredentialAdmin)
admin.site.register(User, UserAdmin)
