from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.tags.models import Label


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True,
                                   null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    executor = models.ForeignKey(CustomUser,
                                 on_delete=models.PROTECT,
                                 related_name='executor_task_set',
                                 blank=True,
                                 null=True
                                 )
    labels = models.ForeignKey(Label,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.PROTECT,
                               related_name='author_task_set'
                               )
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
