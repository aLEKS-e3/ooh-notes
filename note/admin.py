from django.contrib import admin

from note.models import TechTag, Note, NoteGroup

admin.site.register(TechTag)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("owner",)
    list_display = ("title", "owner",)


@admin.register(NoteGroup)
class NoteGroupAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("tag",)
    list_display = ("name", "owner", "tag",)
