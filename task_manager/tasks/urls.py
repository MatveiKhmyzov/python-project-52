from django.urls import path
from .views import (TaskIndex,
                    CreateTask,
                    UpdateTask,
                    DeleteTask,
                    TaskCard)

urlpatterns = [
    path('', TaskIndex.as_view(), name='task_list'),
    path('create/', CreateTask.as_view(), name='create_task'),
    path('<int:pk>/', TaskCard.as_view(), name='task_card'),
    path('<int:pk>/update/', UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete_task')
]
