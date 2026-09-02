from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.prefetch_related("technologies").order_by("order", "-date")
    category = request.GET.get("category", "").strip()
    if category:
        projects = projects.filter(category__iexact=category)
    return render(request, "projects/list.html", {
        "projects": projects,
        "categories": Project.objects.values_list("category", flat=True).distinct().order_by("category"),
        "active_category": category,
    })

def project_detail(request, slug):
    project = get_object_or_404(Project.objects.prefetch_related("technologies","features","gallery"), slug=slug)
    return render(request, "projects/detail.html", {"project": project})
