from django.urls import path
from .views import AddPatientView, PatientDetailView

urlpatterns = [
    path('add/', AddPatientView.as_view(), name='add_patient'),
    path('<int:patient_id>/', PatientDetailView.as_view(), name='patient_detail'),
]
