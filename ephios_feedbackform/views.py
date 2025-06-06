from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from ephios.core.dynamic import dynamic_settings
from ephios.core.services.mail.send import send_mail_template
from guardian.mixins import LoginRequiredMixin

from ephios_feedbackform.forms import FeedbackForm


class FeedbackView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = FeedbackForm
    template_name = "ephios_feedbackform/feedback_form.html"
    success_url = reverse_lazy("ephios_feedbackform:feedback")
    success_message = _("Feedback submitted successfully. Thanks for your help!")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        user_info = _("\n\nsubmitted by: {user} ({email}) at {site}").format(user=self.request.user, email=self.request.user.email, site=dynamic_settings.SITE_URL) if form.cleaned_data["attach_userinfo"] else ""
        path = "\n" + _("Path") + ": " + self.request.GET.get("from", "")
        send_mail_template(
            to=["support@ephios.de"],
            subject=_("Feedback"),
            plaintext=form.cleaned_data["message"] + user_info + path,
            reply_to=[self.request.user.email] if form.cleaned_data["attach_userinfo"] else None,
            is_autogenerated=False,
        )
        return super().form_valid(form)
