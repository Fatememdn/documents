from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import(ListUser,
                    NewUser,
                      UpdateUser,
                        DeleteUser)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', ListUser.as_view()),
    path('newuser/', NewUser.as_view(), name='new-user'),
    path('updateuser/<int:pk>/', UpdateUser.as_view()),
    path('deleteuser/<int:pk>/', DeleteUser.as_view()),
]