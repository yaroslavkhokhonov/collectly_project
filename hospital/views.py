from rest_framework import viewsets

from django.db.models import Sum, F
from rest_framework.response import Response

from hospital.models import Patient, Payment
from hospital.scripts import import_payments, import_patients


class PatientViewSet(viewsets.ViewSet):
    queryset = Patient.objects.all()

    def get(self):
        payment_min = self.request.query_params.get('payment_min')
        payment_max = self.request.query_params.get('payment_max')

        queryset = self.queryset

        if payment_max or payment_min:
            queryset = queryset.annotate(total_ammount=Sum('payments__amount'))

        if payment_min is not None:
            queryset = queryset.filter(total_ammount__gte=payment_min)

        if payment_max is not None:
            queryset = queryset.filter(total_ammount__lte=payment_max)

        return queryset

    def post(self):
        patients = self.request.data.get('patients')

        if not patients:
            return Response(status=400)

        import_patients(patients)
        return Response()


class PaymentViewSet(viewsets.ViewSet):
    queryset = Payment.objects.all()

    def get(self):
        queryset = self.queryset

        patient_ext_id = self.request.query_params.get('external_id')
        if patient_ext_id is not None:
            queryset = (
                queryset
                .annotate(patient_external_id=F('patient__external_id'))
                .filter(patient_external_id=patient_ext_id)
            )

        return queryset

    def post(self):
        payments = self.request.data.get('payments')

        if not payments:
            return Response(status=400)

        import_payments(payments)
        return Response()
