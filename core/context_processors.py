from portfolio.models import Profile, SocialLink


def site_context(request):
    return {
        "profile": Profile.objects.first(),
        "social_links": SocialLink.objects.filter(
            is_active=True
        ).order_by("order", "id"),
    }