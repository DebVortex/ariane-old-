from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WikiConfig(AppConfig):
    """Configuration for wiki app."""

    name = 'ariane.apps.wiki'
    verbose_name = _("Wiki")
