from django.urls import path
from .views import home, search, insert

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('search', search, name='search'),
    path('insert', insert.as_view(), name='insert'),
]