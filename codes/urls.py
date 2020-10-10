from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('code/<code_id>/', code_view, name="code_view"),
]
