
from rest_framework import serializers

from .models import Scenario

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['scenario_number','item','cost','verbiage']
