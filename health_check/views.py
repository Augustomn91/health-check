from django.views.generic import TemplateView
from health_check.models import Application, Status
import requests


# Create your views here.
class ApplicationList(TemplateView):
    model = Application
    template_name = 'health_check/healthcheck.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:


        except Exception as e:
            print(e)


        context['omniproj_name'] = Application.objects.get(name='Omniproj')
        context['omniproj_status'] = Status.objects.get(application__name='Omniproj')

        context['amhdocs_name'] = Application.objects.get(name='AMH Docs')
        context['amhdocs_status'] = Status.objects.get(application__name='AMH Docs')

        context['chatbots_name'] = Application.objects.get(name='Chatbots')
        context['chatbots_status'] = Status.objects.get(application__name='Chatbots')

        context['trilhas_name'] = Application.objects.get(name='Trilhas')
        context['trilhas_status'] = Status.objects.filter(application__name='Trilhas').last()

        context['omni_name'] = Application.objects.get(name='Omni')
        context['omni_status'] = Status.objects.get(application__name='Omni')

        context['auditoriasv1_name'] = Application.objects.get(name='Auditorias v1')
        context['auditoriasv1_status'] = Status.objects.get(application__name='Auditorias v1')

        context['auditoriasv2_name'] = Application.objects.get(name='Auditorias v2')
        context['auditoriasv2_status'] = Status.objects.get(application__name='Auditorias v2')

        context['amhcontas_name'] = Application.objects.get(name='AMH Contas')
        context['amhcontas_status'] = Status.objects.get(application__name='AMH Contas')

        context['siteomni_name'] = Application.objects.get(name='Site Omni')
        context['siteomni_status'] = Status.objects.get(application__name='Site Omni')


        return context



