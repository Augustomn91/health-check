import requests
from django.db import models
from .status import Status
from .choices.name_tags import NameTags


class Application(models.Model):
    name = models.CharField(max_length=128, null=True)
    url = models.URLField()
    name_tag = models.CharField(max_length=25, choices=NameTags.tags(), null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = 'Application'


    @staticmethod
    def status_code(self):
        url = requests.get(self.url)
        status_code_create = Status.objects.create(application=self, code=url.status_code)
        return status_code_create
