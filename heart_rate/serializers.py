from rest_framework import serializers
from .models import HeartRateData

class HeartRateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartRateData
        fields = ['id', 'patient', 'heart_rate', 'recorded_at']
