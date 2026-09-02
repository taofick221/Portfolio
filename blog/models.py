from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=220)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    cover = models.ImageField(upload_to="blog/", blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    def __str__(self): return self.title
