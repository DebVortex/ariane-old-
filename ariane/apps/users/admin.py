from django.contrib import admin

from . import models


class UserSettingsAdmin(admin.ModelAdmin):
    """Admin for UserSetting model."""

    extra = 0
    fields = ('user', 'language',)
    model = models.UserSetting


admin.site.register(models.UserSetting, UserSettingsAdmin)
