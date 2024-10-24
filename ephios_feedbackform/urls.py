from django.urls import path

from ephios_feedbackform.views import FeedbackView

app_name = "ephios_feedbackform"

urlpatterns = [
    path("feedback/", FeedbackView.as_view(), name="feedback"),
]
