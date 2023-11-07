from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','name','description']

    def validate_name(self, value):
        if value.startswith('T') or value.startswith('t'):
            raise serializers.ValidationError("Name should not start with Letter T or t")
        return value