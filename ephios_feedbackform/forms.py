from django import forms
from django.utils.translation import gettext_lazy


class FeedbackForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label=gettext_lazy("Message"))
    attach_userinfo = forms.BooleanField(
        label=gettext_lazy("Attach user information"),
        required=False,
        initial=True,
        help_text=gettext_lazy(
            "Checking this box allows us to see who the feedback is from. This makes it possible for "
            "us to follow up with you if we have any questions. If you do not check this box, the "
            "feedback will be anonymous."
        ),
    )
    path = forms.CharField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        if "initial" not in kwargs:
            kwargs["initial"] = {}
        kwargs["initial"].setdefault("path", self.request.GET.get("from", ""))
        super().__init__(*args, **kwargs)
