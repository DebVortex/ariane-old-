from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    """LandingPage for registering and logging in."""

    template_name = 'frontend/index.html'

    def get(self, request, *args, **kwargs):
        """
        Handle the get request.

        Redirects to ariane if logged in. Otherwise, renders the landingpage.

        Args:
            request (Request): the HTTPRequest for processing.
            *args, **kwargs: additional arguments, used for the inherited views.
        """
        if request.user.is_authenticated():
            response = redirect('ariane')
        else:
            response = super(LandingPageView, self).get(request, *args, **kwargs)
        return response


class ArianeView(LoginRequiredMixin, TemplateView):
    """The core view of the project."""

    template_name = 'frontend/ariane.html'
