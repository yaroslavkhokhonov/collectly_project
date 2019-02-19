from django.utils import timezone

from hospital.models import Payment, Patient


def import_payments(payments):
    _import_records(payments, Payment)


def import_patients(patients):
    _import_records(patients, Patient)


def _import_records(records, model):
    """
    Script for import data from json to table.
    Model must contain date_created, date_updated and external_id fields.
    Also Model must contain `params_from_json` classmethod.
    :param records: json data of imported records.
    :param model: model of imported records.
    """

    existing_ids = set(
        model.objects.all().list_values('external_id', flat=True)
    )
    used_ids = set()
    records_to_create = []
    for record_json in records:
        external_id = record_json['externalId']
        params = model.params_from_json(record_json)
        if external_id in existing_ids:
            (
                model.objects
                .filter(external_id=external_id)
                .update(date_updated=timezone.now(), **params)
            )
        else:
            records_to_create.append(
                model(
                    date_created=timezone.now(),
                    date_updated=timezone.now(),
                    **params
                )
            )
        used_ids.add(external_id)

    (
        model.objects
        .filter(external_id__in=list(existing_ids - used_ids))
        .filter(external_id__is_null=True)
        .delete()
    )
    model.objects.bulk_create(records_to_create)