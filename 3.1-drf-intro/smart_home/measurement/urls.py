from django.urls import path

from .views import SensorView, MasurementView, SensorsView


urlpatterns = [
    path("sensors/", SensorsView.as_view()),
    path("sensors/<id>", SensorView.as_view()),
    path("measurements/", MasurementView.as_view()),
]
