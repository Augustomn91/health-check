from django.db import models


class Status(models.Model):
    application = models.ForeignKey('Application', on_delete=models.CASCADE, related_name='statuses')
    code = models.PositiveIntegerField()

    def __int__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Status'
