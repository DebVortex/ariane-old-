from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    """AppConfig for core app."""

    name = 'ariane.apps.core'
    verbose_name = _("Core")

    def ready(self):
        """Once the ariane core app is loaded, discover and load all brain modules."""
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('brain')
