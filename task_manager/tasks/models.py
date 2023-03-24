from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.tags.models import Tag


class Tasks(models.Model):
    task_name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    executor = models.ForeignKey(CustomUser,
                                 on_delete=models.PROTECT,
                                 related_name='executor_task_set'
                                 )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.PROTECT,
                               related_name='author_task_set'
                               )
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name
