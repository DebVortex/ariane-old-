from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    """LandingPage for registering and logging in."""

    template_name = 'frontend/index.html'


class ArianeView(LoginRequiredMixin, TemplateView):
    """The core view of the project."""

    template_name = 'frontend/ariane.html'
