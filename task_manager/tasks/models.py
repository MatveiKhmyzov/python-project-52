from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True,
                                   null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    executor = models.ForeignKey(CustomUser,
                                 on_delete=models.PROTECT,
                                 related_name='executors',
                                 blank=True,
                                 null=True
                                 )
    labels = models.ManyToManyField(Label,
                                    related_name='tasks',
                                    blank=True)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.PROTECT,
                               related_name='authors'
                               )
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
