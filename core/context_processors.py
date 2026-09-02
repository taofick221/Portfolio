from .models import SiteSettings
from portfolio.models import Profile, SocialLink

def site_context(request):
    return {
        "site_settings": SiteSettings.objects.first(),
        "profile": Profile.objects.first(),
        "social_links": SocialLink.objects.filter(is_active=True).order_by("order"),
    }
