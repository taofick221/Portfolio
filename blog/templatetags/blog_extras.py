import markdown

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_markdown(value):
    if not value:
        return ""

    html = markdown.markdown(
        value,
        extensions=[
            "extra",
            "nl2br",
            "sane_lists",
        ],
    )

    return mark_safe(html)