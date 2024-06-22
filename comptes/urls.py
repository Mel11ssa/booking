from django.urls import path
from .views import TransporteurInscriptionView, ChauffeurInscriptionView, ConnexionView

urlpatterns = [
    path('transporteur/inscription/', TransporteurInscriptionView.as_view(), name='transporteur-inscription'),
    path('chauffeur/inscription/', ChauffeurInscriptionView.as_view(), name='chauffeur-inscription'),
    path('connexion/', ConnexionView.as_view(), name='connexion'),
    # autres URLs
]
