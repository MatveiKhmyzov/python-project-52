from django.urls import path
from .views import (CreateUser,
                    UpdateUser,
                    DeleteUser,
                    UserIndex)

urlpatterns = [
    path('', UserIndex.as_view(), name='user_list'),
    path('<int:pk>/update/', UpdateUser.as_view(), name='update_user'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete_user'),
    path('create/', CreateUser.as_view(), name='create_user'),
]
