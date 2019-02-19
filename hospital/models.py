from django.utils import timezone

from django.db import models


class DateTimeTrackerMixin(models.Model):
    """
    Mixin for storing datetime of object's creation and updating.
    """
    date_created = models.DateTimeField(editable=False)
    date_edited = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.date_created = timezone.now()
        self.date_edited = timezone.now()
        return super(DateTimeTrackerMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Patient(DateTimeTrackerMixin):
    first_name = models.TextField()
    last_name = models.TextField()
    middle_name = models.TextField(null=True)
    date_of_birth = models.DateField(null=True)
    external_id = models.TextField(null=True)

    @classmethod
    def params_from_json(cls, data):
        return {
            'first_name': data.get('firstName'),
            'last_name': data.get('lastName'),
            'middle_name': data.get('middleName'),
            'date_of_birth': data.get('dateOfBirth'),
            'external_id': data.get('externalId'),
        }


class Payment(DateTimeTrackerMixin):
    amount = models.FloatField()
    patient_id = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='payments',
    )
    external_id = models.TextField(null=True)

    @classmethod
    def params_from_json(cls, data):
        return {
            'amount': data.get('amount'),
            'patient_id': data.get('patientId'),
            'external_id': data.get('externalId'),
        }
