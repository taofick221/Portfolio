from django.contrib import admin
from .models import Profile, SocialLink, SkillCategory, Skill, Experience, Education, Research

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "headline", "email", "available_for_work")
    fieldsets = (
        ("Identity", {"fields": ("name", "headline", "photo", "available_for_work")}),
        ("About", {"fields": ("short_bio", "about")}),
        ("Contact", {"fields": ("location", "email", "phone")}),
        ("Resume", {"fields": ("resume",), "description": "Upload the PDF here. The site will automatically show View Resume and Download Resume buttons."}),
    )

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "label", "is_active", "order")
    list_editable = ("is_active", "order")
    ordering = ("order", "id")

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ("name", "icon", "order")

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    inlines = [SkillInline]
    ordering = ("order", "id")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "icon", "order")
    list_filter = ("category",)
    search_fields = ("name", "category__name")
    ordering = ("category", "order", "id")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date", "order")
    ordering = ("order", "-start_date")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "degree", "result", "order")
    ordering = ("order", "-end_date")

@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    search_fields = ("title",)
    ordering = ("order", "id")
