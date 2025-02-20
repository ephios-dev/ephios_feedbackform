from ephios.core.plugins import PluginConfig


class PluginApp(PluginConfig):
    name = "ephios_feedbackform"

    class EphiosPluginMeta:
        name = "Feedback Form"
        author = "Julian Baumann <julian@ephios.de>"
        description = "Feedback form for ephios"
        visible = False
        force_enabled = True

    def ready(self):
        from . import signals  # NOQA
