from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class Profile(models.Model):
    name = models.CharField(max_length=180)
    headline = models.CharField(max_length=220)
    short_bio = models.TextField()
    about = models.TextField()
    location = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)

    photo = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
    )

    resume = models.FileField(
        upload_to="resume/",
        storage=RawMediaCloudinaryStorage(),
        blank=True,
        null=True,
    )

    available_for_work = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ("github", "GitHub"),
        ("linkedin", "LinkedIn"),
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("email", "Email"),
        ("website", "Website"),
    ]

    platform = models.CharField(
        max_length=30,
        choices=PLATFORM_CHOICES,
    )

    label = models.CharField(
        max_length=80,
        blank=True,
    )

    url = models.URLField()

    is_active = models.BooleanField(
        default=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.label or self.get_platform_display()


class SkillCategory(models.Model):
    name = models.CharField(
        max_length=100,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name="skills",
    )

    name = models.CharField(
        max_length=100,
    )

    icon = models.ImageField(
        upload_to="skills/icons/",
        blank=True,
        null=True,
    )

    level = models.PositiveIntegerField(
        default=80,
        help_text="Optional internal value; not shown on the website.",
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    DEFAULT_ICON_MAP = {
        "Python": "img/skills/python.svg",
        "Java": "img/skills/java.svg",
        "JavaScript": "img/skills/javascript.svg",
        "SQL": "img/skills/sql.svg",
        "Django": "img/skills/django.svg",
        "Django REST Framework": "img/skills/drf.svg",
        "PostgreSQL": "img/skills/postgresql.svg",
        "MySQL": "img/skills/mysql.svg",
        "Redis": "img/skills/redis.svg",
        "RESTful APIs": "img/skills/api.svg",
        "JWT Authentication": "img/skills/jwt.svg",
        "Swagger/OpenAPI": "img/skills/swagger.svg",
        "Docker": "img/skills/docker.svg",
        "Docker Compose": "img/skills/docker.svg",
        "Git": "img/skills/git.svg",
        "GitHub": "img/skills/github.svg",
        "Linux": "img/skills/linux.svg",
        "Postman": "img/skills/postman.svg",
    }

    @property
    def default_icon(self):
        return self.DEFAULT_ICON_MAP.get(
            self.name,
            "img/skills/default.svg",
        )

    def __str__(self):
        return self.name


class Experience(models.Model):
    role = models.CharField(
        max_length=150,
    )

    company = models.CharField(
        max_length=150,
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    description = models.TextField()

    order = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return f"{self.role} — {self.company}"


class Education(models.Model):
    institution = models.CharField(
        max_length=180,
    )

    degree = models.CharField(
        max_length=180,
    )

    result = models.CharField(
        max_length=80,
        blank=True,
    )

    start_date = models.DateField(
        blank=True,
        null=True,
    )

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.institution


class Research(models.Model):
    title = models.CharField(
        max_length=300,
    )

    description = models.TextField()

    technologies = models.CharField(
        max_length=300,
        blank=True,
    )

    url = models.URLField(
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    @property
    def technology_list(self):
        return [
            item.strip()
            for item in self.technologies.split(",")
            if item.strip()
        ]

    def __str__(self):
        return self.title