from rest_framework import serializers
from ..models import AstroRegister


class AstroRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstroRegister()
        fields = (
            'id',
            'name',
            'mail'
        )


