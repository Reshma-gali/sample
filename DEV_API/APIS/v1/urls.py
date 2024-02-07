from django.urls import path
from APIS.v1 import views
urlpatterns=[
    path("get_details",views.get_details)
]