from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersConfig(AppConfig):
    """Configuration for users app."""

    name = 'ariane.apps.users'
    verbose_name = _("Users")
