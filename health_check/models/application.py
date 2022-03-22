from django.db import models
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


