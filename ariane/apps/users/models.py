from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserSetting(models.Model):
    """Model to store settings of a user."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='settings',
    )
    language = models.CharField(
        max_length=255,
        default=settings.LANGUAGE_CODE,
        choices=settings.ARIANE_SUPPORTED_LANGUAGES,
    )

    class Meta:
        verbose_name = _("User Setting")
        verbose_name_plural = _("User Settings")

    def update(self, **kwargs):
        """Update UserSetting attributes and save the model."""
        if 'language' in kwargs:
            self.language = kwargs['language']
        self.save()
