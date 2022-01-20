from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ImportFileView, SingleExcelFile, SingleDownloadExcelFile

app_name = "import_api"

urlpatterns = [
    path('import', ImportFileView.as_view()),
    path('import/<int:pk>', SingleExcelFile.as_view()),
    path('download/<int:pk>', SingleDownloadExcelFile.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
