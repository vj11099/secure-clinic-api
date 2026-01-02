from django.db import models


class Medication(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    standard_dose = models.CharField(max_length=100)
    form = models.CharField(max_length=100)

    class Meta:
        db_table = 'Medication'
        indexes = [
            models.Index(fields=['name']),
        ]
