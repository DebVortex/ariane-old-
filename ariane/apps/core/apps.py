from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    """AppConfig for core app."""
    name = 'ariane.apps.core'
    verbose_name = _("Core")
