from django.db import models
from django.urls import reverse

class Technology(models.Model):
    name = models.CharField(max_length=80, unique=True)
    def __str__(self): return self.name

class Project(models.Model):
    STATUS_CHOICES = [("Completed","Completed"),("In Progress","In Progress"),("Planned","Planned"),("Archived","Archived")]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100, default="Web")
    date = models.DateField()
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default="Completed")
    short_description = models.TextField()
    overview = models.TextField()
    thumbnail = models.ImageField(upload_to="projects/thumbnails/", blank=True, null=True)
    live_demo_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    technologies = models.ManyToManyField(Technology, blank=True, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.title
    def get_absolute_url(self): return reverse("project_detail", kwargs={"slug": self.slug})

class ProjectFeature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="features")
    title = models.CharField(max_length=220)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ["order", "id"]
    def __str__(self): return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=220, blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ["order", "id"]
    def __str__(self): return f"{self.project.title} — {self.order}"
