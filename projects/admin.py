from django.contrib import admin
from .models import Technology, Project, ProjectFeature, ProjectImage

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

class FeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1
    ordering = ("order",)

class GalleryInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    ordering = ("order",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date", "status", "featured", "order")
    list_filter = ("status", "category", "featured")
    search_fields = ("title", "short_description", "overview")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("technologies",)
    list_editable = ("featured", "order")
    date_hierarchy = "date"
    inlines = [FeatureInline, GalleryInline]

    fieldsets = (
        ("Basic information", {
            "fields": ("title", "slug", "category", "date", "status", "featured", "order")
        }),
        ("Content", {
            "fields": ("short_description", "overview")
        }),
        ("Media", {
            "fields": ("thumbnail",)
        }),
        ("Links", {
            "fields": ("live_demo_url", "github_url")
        }),
        ("Technology", {
            "fields": ("technologies",)
        }),
    )

@admin.register(ProjectFeature)
class ProjectFeatureAdmin(admin.ModelAdmin):
    list_display = ("project", "title", "order")
    list_filter = ("project",)
    search_fields = ("title", "project__title")

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "caption", "order")
    list_filter = ("project",)
