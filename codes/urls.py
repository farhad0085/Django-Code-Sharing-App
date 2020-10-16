from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('lang/<language_name>/', language_page, name="language_page"),
    path('code/<code_id>/', code_view, name="code_view"),
]
