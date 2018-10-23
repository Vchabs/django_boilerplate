from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import json
from scenario.models import Scenario

class Command(BaseCommand):
    help = 'Loads data'

    def handle(self, *args, **options):
        # Pedantic moment: Atomic transactions means anything you do within the bucket happens as one database transaction
        # When you need to add lots of data, it speeds it up greatly
        # It is not needed really here but only here for pedantic purposes
        with transaction.atomic():
            with open('data/sample_data.json') as f:
                data = json.load(f)
                for i in data:
                    new_scenario = Scenario(
                        scenario_number = i['Scenario Number'],
                        item = i["Item"],
                        cost = i["Cost"],
                        verbiage = i["Verbiage"]
                    )
                    new_scenario.save()