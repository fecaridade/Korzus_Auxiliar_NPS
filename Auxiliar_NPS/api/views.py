from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView
)

from Auxiliar_NPS.models import Client
from .serializers import (
    ClientListSerializer,
    ClientDetailSerializer,
    ClientCreateUpdateSerializer
)


class ClientCreateAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateUpdateSerializer


class ClientDetailAPIView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    lookup_field = 'pk'


class ClientUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ClientDeleteAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    lookup_field = 'pk'


class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer