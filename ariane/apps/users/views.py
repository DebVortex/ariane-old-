from braces.views import LoginRequiredMixin

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

from . import forms, models


class UpdateUserSettingsView(LoginRequiredMixin, FormView):
    """View for the user to update his settings."""

    template_name = 'users/user_settings_update.html'
    form_class = forms.UserSettingForm
    model = models.UserSetting

    def get_object(self):
        """Return the UserSetting of the current user.

        If the user has no related UserSetting, it gets created.

        Returns:
            UserSetting: the UserSetting object of the current user
        """
        self.object, _ = self.model.objects.get_or_create(user=self.request.user)
        return self.object

    def get_form_kwargs(self):
        """Return the keyword arguments for the form.

        Returns:
            Dict: the form keyword arguments, updated with the UserSetting of
            the current user
        """
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.get_object()})
        return kwargs

    def form_valid(self, form):
        """Save new data and redirect back to view."""
        self.object.update(language=form.cleaned_data['language'])
        messages.add_message(self.request, messages.SUCCESS, _("Settings saved."))
        return self.get(self, self.request)
