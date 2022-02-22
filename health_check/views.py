from django.views.generic import ListView
from health_check.models import Application, Status


# Create your views here.
class ApplicationList(ListView):
    model = Application
    template_name = 'health_check/server.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,  **kwargs)

        coding = Application.objects.filter(ativo=True)

        for _codings in coding:
            _codings.saveCodes()
            context['name'] = _codings

        return context
