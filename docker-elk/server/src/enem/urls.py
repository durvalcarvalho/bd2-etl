from django.urls import include, path
from rest_framework import routers

from enem.views import (
    CandidatoModelViewSet,
    MunicipioModelViewSet,
    ProvaModelViewSet,
    RealizaModelViewSet,
)


router = routers.DefaultRouter()

router.register("candidatos", CandidatoModelViewSet)
router.register("municipios", MunicipioModelViewSet)
router.register("provas", ProvaModelViewSet)
router.register("realizas", RealizaModelViewSet)


urlpatterns = [
    path("", include(router.urls)),
]