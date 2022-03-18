from django.views.generic import TemplateView
from health_check.models import Application, Status
import requests


# Create your views here.
class ApplicationList(TemplateView):
    model = Application
    template_name = 'health_check/healthcheck.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['omniproj_name'] = Application.objects.get(name='Omniproj')
        context['omniproj_status'] = Status.objects.get(application__name='Omniproj')

        return context



