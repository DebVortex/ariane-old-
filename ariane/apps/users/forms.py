from django import forms

from . import models


class UserSettingForm(forms.ModelForm):
    """Form to update UserSetting."""

    class Meta:
        model = models.UserSetting
        fields = ['language']
