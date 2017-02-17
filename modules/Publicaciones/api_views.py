from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
#from .serializers import UserSerializer,UserSecondSerializer
# PARA LA SEGUNDA clase
from .serializers import *
from django.shortcuts import get_object_or_404

#Vistas basadas en clases

class UserList(APIView):
    
    def get(self,request):
        #Se pide todo los usuarios
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        #Se crea el usuario
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Métodos para completar el CRUD
class UserDetail(APIView):

    #
    def get(self, request, pk):

        user = get_object_or_404(User,pk=pk)

        if user is not None:
            serializer = UserFirstSerializer(user)
            return Response(serializer.data, status = status.HTTP_200_OK)

    # Para modificar un registro individual de usuario en la base
    def put(self, request,pk):
        user = get_object_or_404(User,pk=pk)

        if user is not None:
            serializer = UserFirstSerializer(instance=user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User,pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
