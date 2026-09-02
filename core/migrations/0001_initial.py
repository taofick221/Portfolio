from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="SiteSettings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("site_name", models.CharField(default="Taofick Portfolio", max_length=120)),
                ("tagline", models.CharField(blank=True, max_length=220)),
                ("footer_text", models.CharField(blank=True, max_length=220)),
                ("accent_label", models.CharField(default="Backend Developer", max_length=80)),
                ("seo_title", models.CharField(blank=True, max_length=160)),
                ("seo_description", models.TextField(blank=True)),
            ],
        ),
    ]
