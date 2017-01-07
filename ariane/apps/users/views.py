from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


class UpdateUserSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_settings_update.html'
