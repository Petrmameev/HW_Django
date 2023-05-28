from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import (
    SensorDetailSerializer,
    SensorSerializer,
    MeasurementSerializer,
    MeasurementDetailSerializer,
)


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor.objects.create(
            name=request.POST.get("name"), description=request.POST.get("description")
        )
        return Response({"status": "ok"})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.object.get(id=pk)
        sensor.description = request.data["description"]
        sensor.save()
        return Response({"status": "ok"})


class MasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer

    def post(self, request):
        Measurement.objects.create(
            sensor_id=request.POST.get("sensor"),
            temperature=request.POST.get("temperature"),
        )
        return Response({"status": "ok"})
