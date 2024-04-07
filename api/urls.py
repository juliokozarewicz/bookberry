from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import book_viewset

app_name = 'api'

router = DefaultRouter()
router.register(r'api', book_viewset, basename='books')

urlpatterns = [
    path('', include(router.urls)),
]