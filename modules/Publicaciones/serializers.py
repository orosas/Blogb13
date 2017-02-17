from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Publicacion
#from modules.Publicaciones.serializers import PublicacionSerializer

# para tablas que están relacionadas
# es la tercera clase del ejemplo, pero se mueve al principio
class PublicacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publicacion
        fields = ('nombre', 'contenido', 'fecha', 'tags')

class UserFirstSerializer(serializers.ModelSerializer):

    publicaciones = PublicacionSerializer(read_only=True,many=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'is_active',
            'publicaciones'
            )
        #todos los campos field = ('__ALL__')
class UserSecondSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_active',)

