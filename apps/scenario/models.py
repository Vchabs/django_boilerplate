import uuid
from django.db import models
from lib.model_stamps import RowStatusModel


class Scenario(RowStatusModel):

    #Note this is intentional - Typically your primary key should not be the same as a natural key. Always make it different.
    # UUID Fields are great if you have a ton of data, otherwise an AutoField is preferable (uses less space...indexes can be smaller, but UUID fields are small enough)
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column = 'scenario_id')

    scenario_number = models.IntegerField(db_column='scenario_number')
    item = models.TextField(db_column='item')
    cost = models.IntegerField(db_column='cost')
    verbiage = models.TextField(db_column='verbiage')

    class Meta:
        db_table = 'scenario'
