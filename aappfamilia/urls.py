from django.urls import path
from aappfamilia.views import mostrar_familia

urlpatterns = [
    path("persona/", mostrar_familia)
]

