from django.urls import path
from .views import home, search, insert, delete

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('search', search.as_view(), name='search'),
    path('insert', insert.as_view(), name='insert'),
    path('delete/<int:pk>', delete.as_view(), name='delete'),
]