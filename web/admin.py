from django.contrib             import admin
from django.contrib.auth.admin  import UserAdmin
from .models                    import User, ServiceRequest

# Custom User Admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    # Display these fields in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'address', 'is_staff', 'is_active')

    # Fields to be searchable in the admin search bar
    search_fields = ('email', 'username', 'phone', 'address')

    # Default ordering for the list view
    ordering = ('email',)

    # Fieldsets to customize the admin form (adding phone and address fields)
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('phone', 'address')}),
    )

    # Fields that appear in the 'Add User' form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {'fields': ('phone', 'address')}),
    )

    # Customize form for user creation
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

# Custom ServiceRequest Admin
@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display    = ('user', 'request_type', 'status', 'created_at', 'updated_at')
    search_fields   = ('request_type', 'status', 'user__username')
    list_filter     = ('status', 'created_at')
    ordering        = ('-created_at',)