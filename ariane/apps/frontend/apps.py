from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FrontendConfig(AppConfig):
    """Configuration for frontend app."""

    name = 'ariane.apps.frontend'
    verbose_name = _("Frontend")
