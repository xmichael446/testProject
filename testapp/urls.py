from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

from testapp.views import Calculate

urlpatterns = [
    path("get-token/", obtain_auth_token, name="get-token"),
    path("calculate/", Calculate.as_view(), name="calculate"),
]