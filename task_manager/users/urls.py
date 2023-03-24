from django.urls import path
from .views import (CreateUser,
                    UpdateUser,
                    DeleteUser,
                    LoginUser,
                    LogoutUser,
                    UserIndex)

urlpatterns = [
    path('', UserIndex.as_view(), name='user_list'),
    path('<int:pk>/update', UpdateUser.as_view(), name='update_user'),
    path('<int:pk>/delete', DeleteUser.as_view(), name='delete_user'),
    path('create', CreateUser.as_view(), name='create_user'),
    path('login', LoginUser.as_view(), name='login_user'),
    path('logout', LogoutUser.as_view(), name='logout_user'),
]
