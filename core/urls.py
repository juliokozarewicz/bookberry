from django.urls import path
from .views import home, search, insert, delete, edit

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('search', search.as_view(), name='search'),
    path('insert', insert.as_view(), name='insert'),
    path('edit/<int:pk>', edit.as_view(), name='edit'),
    path('delete/<int:pk>', delete.as_view(), name='delete'),
]