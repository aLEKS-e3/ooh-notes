from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from note.models import TechTag, Note
from users.models import TechUser

admin.site.register(TechTag)


@admin.register(TechUser)
class TechUserAdmin(UserAdmin):
    search_fields = ("username",)
    list_filter = ("skill",)
    list_display = UserAdmin.list_display + ("skill",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("skill",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "skill",
                    )
                },
            ),
        )
    )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("owner",)
    list_display = ("title", "owner",)
