from django.urls import path
from .views import AddHeartRateDataView, HeartRateDataDetailView

urlpatterns = [
    path('add/<int:patient_id>/', AddHeartRateDataView.as_view(), name='add_heart_rate_data'),
    path('<int:patient_id>/', HeartRateDataDetailView.as_view(), name='heart_rate_data_detail'),
]
