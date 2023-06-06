from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
)

from .models import Sensor, Measurement
from .serializers import (
    SensorDetailSerializer,
    SensorSerializer,
    MeasurementDetailSerializer,
)


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = "id"


class MasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer
