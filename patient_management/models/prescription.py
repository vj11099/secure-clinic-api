from .user import User
from .encounter import Encounter
from .medication import Medication
from django.db import models


class PrescriptionQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def by_doctor(self, value):
        return self.filter(encounter__doctor_id=value)

    def between_dates(self, start_date, end_date):
        return self.filter(
            start_date__gte=start_date,  # greater than or equal to
            start_date__lte=end_date)   # less than or equal to


class Prescription(models.Model):
    encounter = models.ForeignKey(Encounter, on_delete=models.PROTECT)
    medication = models.ForeignKey(Medication, on_delete=models.PROTECT)
    dose = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    duration_days = models.IntegerField()
    start_date = models.DateField(db_index=True)
    instructions = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='created_prescription_by_user')
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='updated_prescription_by_user')
    objects = PrescriptionQuerySet.as_manager()

    class Meta:
        db_table = 'Prescription'
        indexes = [
            models.Index(fields=['encounter', 'is_active']),
            models.Index(fields=['start_date']),
            models.Index(fields=['is_active'])
        ]
