from django.db import models
from patients.models import Patient

class HeartRateData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="heart_rate_data")
    heart_rate = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Heart rate {self.heart_rate} for {self.patient.name}"
