from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.labels.models import Label
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=30, unique=True)
    description = models.TextField(verbose_name=_('Description'), blank=True,
                                   null=True)
    status = models.ForeignKey(Status, verbose_name=_('Status'), on_delete=models.CASCADE)
    executor = models.ForeignKey(CustomUser,
                                 verbose_name=_('Executor'),
                                 on_delete=models.PROTECT,
                                 related_name='executors',
                                 blank=True,
                                 null=True
                                 )
    labels = models.ManyToManyField(Label,
                                    verbose_name=_('Labels'),
                                    related_name='tasks',
                                    blank=True)
    author = models.ForeignKey(CustomUser,
                               verbose_name=_('Author'),
                               on_delete=models.PROTECT,
                               related_name='authors'
                               )
    date_create = models.DateTimeField(verbose_name=_('Data of creation'), auto_now_add=True)

    def __str__(self):
        return self.name
