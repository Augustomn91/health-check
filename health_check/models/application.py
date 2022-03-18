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


    # @staticmethod
    # def status_code(self):
    #     url = requests.get(self.url)
    #     codes = Status.objects.create(application=self, code=url.status_code)
    #     return codes
