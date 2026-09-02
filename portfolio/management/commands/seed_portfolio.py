from django.core.management.base import BaseCommand
from portfolio.models import Profile, SocialLink, SkillCategory, Skill, Education, Research
from projects.models import Technology, Project, ProjectFeature

class Command(BaseCommand):
    help = "Seed portfolio content from the supplied resume."

    def handle(self, *args, **options):
        profile, _ = Profile.objects.update_or_create(
            name="MD. TAOFICK MAHMOODUR RAHAMAN",
            defaults={
                "headline":"Backend-focused Software Engineering Student",
                "short_bio":"Backend-focused Software Engineering student with hands-on experience building production-ready RESTful APIs using Python, Django, and Django REST Framework.",
                "about":"Backend-focused Software Engineering student with hands-on experience building production-ready RESTful APIs using Python, Django, and Django REST Framework. Strong understanding of API design, relational database modeling, and clean architecture with a passion for building secure, maintainable and high-performance applications.",
                "location":"Dhaka, Bangladesh","email":"rahaman35-847@diu.edu.bd","phone":"+8801690206027","available_for_work":True
            }
        )
        SocialLink.objects.update_or_create(platform="github", defaults={"label":"GitHub","url":"https://github.com/","is_active":True,"order":1})
        SocialLink.objects.update_or_create(platform="linkedin", defaults={"label":"LinkedIn","url":"https://www.linkedin.com/","is_active":True,"order":2})
        SocialLink.objects.update_or_create(platform="email", defaults={"label":"Email","url":"mailto:rahaman35-847@diu.edu.bd","is_active":True,"order":3})

        skill_data = {
            "Programming":["Python","Java","JavaScript","SQL"],
            "Frameworks":["Django","Django REST Framework"],
            "Databases":["PostgreSQL","MySQL","Redis"],
            "API":["RESTful APIs","JWT Authentication","Swagger/OpenAPI"],
            "Tools":["Docker","Docker Compose","Git","GitHub","Linux","Postman"],
        }
        for ci, (cat_name, skills) in enumerate(skill_data.items()):
            cat, _ = SkillCategory.objects.update_or_create(name=cat_name, defaults={"order":ci})
            for si, name in enumerate(skills):
                Skill.objects.update_or_create(
                    category=cat,
                    name=name,
                    defaults={
                        "level": 85,
                        "order": si,
                        "icon": None
                    }
                )

        Education.objects.update_or_create(
            institution="Daffodil International University",
            degree="BSc in Software Engineering",
            defaults={"result":"CGPA 3.64/4.00","end_date":"2026-08-01","description":"Expected graduation August 2026.","order":1}
        )
        Research.objects.update_or_create(
            title="A Comparative Study of Hybrid Machine Learning Approaches for Multiclass Bangla Hate Speech Detection",
            defaults={"description":"Comparative research using Python, TensorFlow, Scikit-learn, TF-IDF and SMOTE.","technologies":"Python, TensorFlow, Scikit-learn, TF-IDF, SMOTE","order":1}
        )

        techs = {}
        for name in ["Python","Django","Django REST Framework","PostgreSQL","Redis","Celery","Docker","PHP","MySQL","JavaScript","Bootstrap"]:
            techs[name], _ = Technology.objects.get_or_create(name=name)

        projects = [
            {
                "title":"CoreCommerce","slug":"corecommerce",
                "category":"Backend API","date":"2025-01-01","status":"Completed",
                "short_description":"Production-ready e-commerce backend API built with Django REST Framework.",
                "overview":"A modular e-commerce backend focused on secure APIs, relational data modeling, background jobs, caching and maintainable architecture.",
                "featured":True,"order":1,
                "technologies":["Python","Django","Django REST Framework","PostgreSQL","Redis","Celery","Docker"],
                "features":["Modular apps for authentication, products, carts, orders, payments, shipping and coupons","JWT authentication, role-based access and custom permissions","Service Layer and Selector Pattern for clean architecture","PostgreSQL, Redis, Celery and Docker integration","Filtering, search, pagination, validation and centralized exception handling","Swagger/OpenAPI documentation and unit tests"]
            },
            {
                "title":"Super Shop Management System","slug":"super-shop-management-system",
                "category":"Web","date":"2024-01-01","status":"Completed",
                "short_description":"Inventory and sales management system with an admin dashboard.",
                "overview":"A web-based management system for products, customers, inventory, sales and reporting.",
                "featured":True,"order":2,
                "technologies":["PHP","MySQL","JavaScript","Bootstrap"],
                "features":["Inventory and product management","Customer and order management","Authentication and CRUD workflows","Reports and administrative dashboard"]
            },
            {
                "title":"Bus Booking System","slug":"bus-booking-system",
                "category":"Web","date":"2024-01-01","status":"Completed",
                "short_description":"Online bus ticket reservation and seat booking system.",
                "overview":"A responsive booking platform covering routes, trips, seats and administrative workflows.",
                "featured":True,"order":3,
                "technologies":["PHP","MySQL","JavaScript","Bootstrap"],
                "features":["Online ticket reservation","Interactive seat booking","Route and trip scheduling","Admin dashboard and booking workflows"]
            },
        ]
        for data in projects:
            p, _ = Project.objects.update_or_create(slug=data["slug"], defaults={k:v for k,v in data.items() if k not in ["technologies","features"]})
            p.technologies.set([techs[t] for t in data["technologies"]])
            p.features.all().delete()
            ProjectFeature.objects.bulk_create([ProjectFeature(project=p,title=f,order=i) for i,f in enumerate(data["features"],1)])

        self.stdout.write(self.style.SUCCESS("Portfolio content seeded successfully. Upload your profile photo and resume from Django Admin."))
