from rest_framework import viewsets
from .serializers import book_serializer
from core.models import booksDataBase

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class book_viewset(viewsets.ModelViewSet):
    serializer_class = book_serializer
    queryset = booksDataBase.objects.all()
    authentication_classes = (BasicAuthentication, )
    permission_classes = [IsAuthenticated]  # Requer autenticação para todas as ações

    # Sobrescreva o método get_queryset para filtrar os objetos pelo usuário autenticado
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
