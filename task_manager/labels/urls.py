from django.urls import path
from .views import (LabelIndex,
                    UpdateLabel,
                    CreateLabel,
                    DeleteLabel)

urlpatterns = [
    path('', LabelIndex.as_view(), name='label_list'),
    path('<int:pk>/update/', UpdateLabel.as_view(), name='update_label'),
    path('<int:pk>/delete/', DeleteLabel.as_view(), name='delete_label'),
    path('create/', CreateLabel.as_view(), name='create_label')
]
