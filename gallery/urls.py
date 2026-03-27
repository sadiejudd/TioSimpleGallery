from django.urls import path
from .views import UploadView, HomeView

urlpatterns = [
    path("upload/",UploadView.as_view(), name = "upload"),
    path("", HomeView.as_view())
]