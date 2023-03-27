from django.urls import path
from .views import (StatusIndex,
                    UpdateStatus,
                    CreateStatus,
                    DeleteStatus)

urlpatterns = [
    path('', StatusIndex.as_view(), name='status_list'),
    path('<int:pk>/update', UpdateStatus.as_view(), name='update_status'),
    path('<int:pk>/delete', DeleteStatus.as_view(), name='delete_status'),
    path('create', CreateStatus.as_view(), name='create_status'),
    # path('login', LoginUser.as_view(), name='login_user'),
    # path('logout', LogoutUser.as_view(), name='logout_user'),
]
