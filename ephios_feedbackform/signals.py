from django.dispatch import receiver
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from ephios.core.signals import footer_link


@receiver(footer_link, dispatch_uid="ephios.plugins.files.signals.nav_link")
def add_footer_link(sender, request, **kwargs):
    return {_("Feedback"): reverse_lazy("ephios_feedbackform:feedback")}
