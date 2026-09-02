from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Technology",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(unique=True)),
                ("category", models.CharField(default="Web", max_length=100)),
                ("date", models.DateField()),
                ("status", models.CharField(choices=[("Completed","Completed"),("In Progress","In Progress"),("Planned","Planned"),("Archived","Archived")], default="Completed", max_length=40)),
                ("short_description", models.TextField()),
                ("overview", models.TextField()),
                ("thumbnail", models.ImageField(blank=True, null=True, upload_to="projects/thumbnails/")),
                ("live_demo_url", models.URLField(blank=True)),
                ("github_url", models.URLField(blank=True)),
                ("featured", models.BooleanField(default=False)),
                ("order", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("technologies", models.ManyToManyField(blank=True, related_name="projects", to="projects.technology")),
            ],
            options={"ordering": ["order", "-date"]},
        ),
        migrations.CreateModel(
            name="ProjectFeature",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=220)),
                ("order", models.PositiveIntegerField(default=0)),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="features", to="projects.project")),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="ProjectImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to="projects/gallery/")),
                ("caption", models.CharField(blank=True, max_length=220)),
                ("order", models.PositiveIntegerField(default=0)),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="gallery", to="projects.project")),
            ],
            options={"ordering": ["order", "id"]},
        ),
    ]
