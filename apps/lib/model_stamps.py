from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
import os

class RowStatusModelManager(models.Manager):
	#slight speedup for all querysets by removing all the row fields from the query, 
	def get_queryset(self):
		qs = super(RowStatusModelManager,self).get_queryset()
		qs = qs.defer('row_create_usr_id','row_lup_usr_id')
		return qs


class RowStatusModel(models.Model):

    row_create_ts = AutoCreatedField(db_column = 'row_create_ts')
    row_lup_ts = AutoLastModifiedField(db_column = 'row_lup_ts')
    row_end_ts = models.DateTimeField(default='9999-12-31 00:00:00.00000-00', db_column = 'row_end_ts')
    row_ef = models.BooleanField(default=True, db_column = 'row_ef')
    row_create_usr_id = models.CharField(default=os.environ['USER_ID'],max_length=20, db_column = 'row_create_usr_id')
    row_lup_usr_id = models.CharField(default=os.environ['USER_ID'],max_length=20, db_column = 'row_lup_usr_id')

    class Meta:
        abstract = True

