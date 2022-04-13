from rest_framework.serializers import ModelSerializer

from Auxiliar_NPS.models import Client


class ClientCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'phone_number',
            'rating_nps',
            'partener',
        ]


class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'phone_number',
            'rating_nps',
            'partener',
        ]


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'phone_number',
            'rating_nps',
            'partener',
        ]