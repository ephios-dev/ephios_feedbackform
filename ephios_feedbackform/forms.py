from django import forms
from django.utils.translation import gettext_lazy


class FeedbackForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Message")
    attach_userinfo = forms.BooleanField(label="Attach user information", required=False, initial=True, help_text=gettext_lazy("Checking this box allows us to see who the feedback is from. This makes it possible for us to follow up with you if we have any questions. If you do not check this box, the feedback will be anonymous."))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
