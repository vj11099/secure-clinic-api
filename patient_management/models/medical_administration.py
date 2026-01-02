from .user import User
from .prescription import Prescription
from django.db.models import (
    Model, ForeignKey, DateTimeField,
    CharField, TextField, CASCADE,
    PROTECT, Index)


class MedicalAdministration(Model):
    prescription = ForeignKey(
        Prescription, on_delete=CASCADE,
        related_name='administered_prescription')
    nurse = ForeignKey(User, on_delete=PROTECT,
                       related_name='administration_nurse')
    administered_at = DateTimeField(db_index=True)
    dose_given = CharField(max_length=200)
    notes = TextField(blank=True, null=True)

    class Meta:
        db_table = 'MedicalAdministration'
        indexes = [
            Index(fields=['prescription', 'administered_at'])
        ]
