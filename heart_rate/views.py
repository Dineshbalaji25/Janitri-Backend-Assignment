from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from patients.models import Patient
from .models import HeartRateData
from .serializers import HeartRateDataSerializer

# Add heart rate data
class AddHeartRateDataView(APIView):
    def post(self, request, patient_id):
        heart_rate = request.data.get('heart_rate')
        patient = Patient.objects.get(id=patient_id)

        heart_rate_data = HeartRateData.objects.create(patient=patient, heart_rate=heart_rate)
        serializer = HeartRateDataSerializer(heart_rate_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Get heart rate data
class HeartRateDataDetailView(APIView):
    def get(self, request, patient_id):
        heart_rate_data = HeartRateData.objects.filter(patient_id=patient_id)
        if heart_rate_data.exists():
            serializer = HeartRateDataSerializer(heart_rate_data, many=True)
            return Response(serializer.data)
        return Response({"error": "No heart rate data found"}, status=status.HTTP_404_NOT_FOUND)
