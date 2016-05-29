from braces.views import LoginRequiredMixin

from django.shortcuts import redirect
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'frontend/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            response = redirect('ariane')
        else:
            response = super(LandingPageView, self).get(request, *args, **kwargs)
        return response


class ArianeView(LoginRequiredMixin, TemplateView):
    template_name = 'frontend/ariane.html'
