from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Transporteur, Chauffeur
from django.contrib.auth import authenticate
from .serializers import TransporteurSerializer, ChauffeurSerializer
from rest_framework import generics, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Transporteur, Chauffeur
from .serializers import TransporteurSerializer, ChauffeurSerializer, ConnexionSerializer

from django.contrib.auth.models import User
from .models import Transporteur

from django.db import IntegrityError

class TransporteurInscriptionView(generics.CreateAPIView):
    queryset = Transporteur.objects.all()
    serializer_class = TransporteurSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            # Vérifier si le username est déjà utilisé
            if User.objects.filter(username=serializer.validated_data['username']).exists():
                return Response({'error': 'Ce nom d\'utilisateur est déjà utilisé.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Créer un transporteur
            transporteur = Transporteur.objects.create(
                nom=serializer.validated_data.get('nom'),
                prenom=serializer.validated_data.get('prenom'),
                raison_sociale=serializer.validated_data.get('raison_sociale'),
                tel_tax=serializer.validated_data.get('tel_tax'),
                nif=serializer.validated_data.get('nif'),
                numero_rs=serializer.validated_data.get('numero_rs'),
                numero_bt_camion=serializer.validated_data.get('numero_bt_camion'),
            )
            
            # Créer un utilisateur associé au transporteur
            user = User.objects.create_user(
                username=serializer.validated_data.get('username'),
                email=serializer.validated_data.get('email'),
                password=serializer.validated_data.get('password'),
            )

            return Response({'success': 'Transporteur inscrit avec succès'}, status=status.HTTP_201_CREATED)
        
        except IntegrityError:
            return Response({'error': 'Erreur lors de l\'inscription du transporteur'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from django.db import IntegrityError

class ChauffeurInscriptionView(generics.CreateAPIView):
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            # Vérifier si le username est déjà utilisé
            if User.objects.filter(username=serializer.validated_data['username']).exists():
                return Response({'error': 'Ce nom d\'utilisateur est déjà utilisé.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Créer un chauffeur
            chauffeur = Chauffeur.objects.create(
                nom=serializer.validated_data.get('nom'),
                prenom=serializer.validated_data.get('prenom'),
                numero_pc=serializer.validated_data.get('numero_pc'),
                date_pc=serializer.validated_data.get('date_pc'),
            )
            
            # Créer un utilisateur associé au chauffeur
            user = User.objects.create_user(
                username=serializer.validated_data.get('username'),
                email=serializer.validated_data.get('email'),
                password=serializer.validated_data.get('password'),
            )

            return Response({'success': 'Chauffeur inscrit avec succès'}, status=status.HTTP_201_CREATED)
        
        except IntegrityError:
            return Response({'error': 'Erreur lors de l\'inscription du chauffeur'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework.views import APIView

class ConnexionView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ConnexionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            return Response({'id_utilisateur': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Nom d\'utilisateur ou mot de passe incorrect.'}, status=status.HTTP_400_BAD_REQUEST)