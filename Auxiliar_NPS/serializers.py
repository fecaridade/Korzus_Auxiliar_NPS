
from rest_framework import serializers

from .models import Partner

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ['id', 'email', 'username','first_name', 'last_name']