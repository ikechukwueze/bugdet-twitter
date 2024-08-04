from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import AccountChangeForm, AccountCreationForm
from .models import Account

# Register your models here.


class AccountAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm

    list_display = [
        "email",
        "username",
        "signup_date",
        "last_login",
        "is_admin",
        "is_active",
        "is_verified",
    ]
    list_filter = ["is_admin", "is_active", "is_verified"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "username",
                    "is_admin",
                    "is_active",
                    "password",
                    "profile_pic",
                    "display_name",
                    "bio",
                ]
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "username",
                    "is_admin",
                    "password1",
                    "password2",
                    "profile_pic",
                    "display_name",
                    "bio",
                ],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
