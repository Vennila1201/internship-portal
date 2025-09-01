from django.contrib import admin
from django.utils.html import format_html
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "resume_link", "submitted_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("submitted_at",)

    def resume_link(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank">📂 Download</a>', obj.resume.url)
        return "No file"
    resume_link.short_description = "Resume"
