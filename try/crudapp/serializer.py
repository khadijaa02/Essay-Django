from rest_framework import serializers
from .models import CrudEssay

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudEssay
        fields = ['id', 'field']