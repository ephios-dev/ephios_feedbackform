from django.dispatch import receiver
from django.urls import reverse_lazy, NoReverseMatch, reverse
from django.utils.translation import gettext_lazy as _
from ephios.core.signals import footer_link


@receiver(footer_link, dispatch_uid="ephios.plugins.files.signals.nav_link")
def add_footer_link(sender, request, **kwargs):
    try:
        return {_("Feedback"): reverse("ephios_feedbackform:feedback", query={"from":request.path})} if request.user.is_authenticated else {}
    except NoReverseMatch:
        return {}
