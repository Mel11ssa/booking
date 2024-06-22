from rest_framework import serializers
from .models import Transporteur, Chauffeur
from django.contrib.auth.models import User

class TransporteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporteur
        fields = ('nom', 'prenom','username' ,'raison_sociale', 'tel_tax', 'email', 'nif', 'numero_rs', 'numero_bt_camion', 'password', 'confirm_password')

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")

        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        return user

class ChauffeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = ('nom', 'prenom','username', 'numero_pc', 'date_pc', 'password', 'confirm_password')

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")

        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        return user


from rest_framework import serializers
from django.contrib.auth import authenticate


class ConnexionSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Nom d'utilisateur ou mot de passe incorrect.")
        else:
            raise serializers.ValidationError("Veuillez fournir un nom d'utilisateur et un mot de passe.")

        data['user'] = user  # Ajouter l'utilisateur authentifié à validated_data
        return data
