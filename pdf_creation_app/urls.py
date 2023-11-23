from django.urls import path
from .views import *

urlpatterns = [
    path('pdf/',PdfCreation.as_view()),
]
