from django.urls import path
from .views import image_upload, clear_results

urlpatterns = [
    path('image_upload/', image_upload, name='image_upload'),
    path('clear_results/', clear_results, name='clear_results'),
]
