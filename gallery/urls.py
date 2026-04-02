from django.urls import path
from .views import UploadView, HomeView, ImageDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("upload/",UploadView.as_view(), name = "upload"),
    path("", HomeView.as_view(), name = "home"),
    path("image/<int:pk>", ImageDetailView.as_view(), name = "image_detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)