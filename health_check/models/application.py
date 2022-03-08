import requests
from django.db import models
from .status import Status


class Application(models.Model):
    name = models.CharField(max_length=128, null=True)
    url = models.URLField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = 'Application'

    # método para criar os códigos no modelo de 'Status'
    def saveCodes(self):
        r = requests.get(self.url)
        if r.status_code >= 400:
            Status.objects.create(application=self, code=r.status_code)
