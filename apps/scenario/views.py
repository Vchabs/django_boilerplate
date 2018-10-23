from rest_framework import viewsets
from .serializers import ScenarioSerializer
from .filters import ScenarioFilterSet
from .models import Scenario

class ScenarioViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Scenario.objects.only("scenario_number","item","cost","verbiage")
    serializer_class = ScenarioSerializer
    filter_class = ScenarioFilterSet

