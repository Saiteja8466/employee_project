from rest_framework import viewsets
from .models import Performance
from .serializers import PerformanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all().order_by('id')
    serializer_class = PerformanceSerializer
