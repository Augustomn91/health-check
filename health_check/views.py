from django.views.generic import TemplateView
from health_check.models import Application


# Create your views here.
class ApplicationList(TemplateView):
    model = Application
    template_name = 'health_check/server.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,  **kwargs)



        return context
