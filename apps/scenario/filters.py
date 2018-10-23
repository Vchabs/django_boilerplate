import django_filters

from .models import Scenario

class ScenarioFilterSet(django_filters.FilterSet):
	#Basic search filters...can add more as needed though
	# item=django_filters.CharFilter(name="item",lookup_type='iregex')
	# verbiage = django_filters.CharFilter(name="verbiage",lookup_type='iregex')

	class Meta:
		model=Scenario
		fields=['item','verbiage']