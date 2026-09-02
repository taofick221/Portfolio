from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=220)),
                ("slug", models.SlugField(unique=True)),
                ("excerpt", models.TextField(blank=True)),
                ("content", models.TextField()),
                ("cover", models.ImageField(blank=True, null=True, upload_to="blog/")),
                ("published_at", models.DateTimeField(blank=True, null=True)),
                ("is_published", models.BooleanField(default=False)),
            ],
        ),
    ]
