from django.shortcuts import render, redirect
from portfolio.models import Profile, SkillCategory, Experience, Education, Research
from projects.models import Project
from contact.models import ContactInfo

def home(request):
    return render(request, "core/home.html", {
        "profile_obj": Profile.objects.first(),
        "skills": SkillCategory.objects.prefetch_related("skills").all(),
        "experience": Experience.objects.all(),
        "education": Education.objects.all(),
        "research": Research.objects.all(),
        "featured_projects": Project.objects.filter(featured=True).prefetch_related("technologies").order_by("order", "-date"),
        "contact_info": ContactInfo.objects.first(),
    })


def resume(request):
    profile = Profile.objects.first()
    if not profile or not profile.resume:
        return render(request, "core/resume.html", {"profile_obj": profile, "resume_available": False})
    return render(request, "core/resume.html", {"profile_obj": profile, "resume_available": True})
