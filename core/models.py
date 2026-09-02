from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=120, default="Taofick Portfolio")
    tagline = models.CharField(max_length=220, blank=True)
    footer_text = models.CharField(max_length=220, blank=True)
    accent_label = models.CharField(max_length=80, default="Backend Developer")
    seo_title = models.CharField(max_length=160, blank=True)
    seo_description = models.TextField(blank=True)

    def __str__(self):
        return self.site_name
