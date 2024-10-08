from dj_rest_auth.views import (
    UserDetailsView,
)
from django.urls import path, include
from rest_framework import routers

from apps.users_management.view.user_view import (
    user_information,
    user_update,
    check_unique_email,
    check_unique_username,
)

route = routers.DefaultRouter()
# route.register("users", UserViewSet)
urlpatterns = [
    path("", include(route.urls)),
    path("check_unique_username/", check_unique_username),
    path("check_unique_email/", check_unique_email),
    path("current-user/", user_information, name="current-user"),
    path("user_details/", UserDetailsView.as_view(), name="rest_user_details"),
    path("user_update/<int:id>/", user_update),
]
