from django.urls import path
from .views import VideoDataView

urlpatterns = [
    path('video/', VideoDataView.as_view(), name='video_data'),
]
