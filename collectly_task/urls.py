from django.conf.urls import url, include
from rest_framework import routers

from hospital.views import PatientViewSet, PaymentViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
