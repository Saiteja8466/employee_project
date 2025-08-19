# DRF ViewSet (already unna code)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Performance
from .serializers import PerformanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['employee__name', 'review_date', 'rating']

# Template-based chart view (for /charts/ route)
from django.shortcuts import render
from employees.models import Employee

def performance_chart(request):
    employees = Performance.objects.all()
    labels = [emp.name for emp in employees]
    scores = [emp.performance.rating if hasattr(emp, 'performance') else 0 for emp in employees]
    return render(request, 'charts.html', {'performances': performances})
from django.shortcuts import render
from .models import Performance


