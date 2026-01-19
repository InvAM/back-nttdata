from django.shortcuts import render
from rest_framework.views import APIView

from apps.users.serializers import UserSerializer
from apps.users.services.api import RandomUserService
from rest_framework.response import Response
# Create your views here

class GenerateUsersAPIView(APIView):
    
    def post(self):
        users_data = RandomUserService.get_users(results=10)
        
        created_users = []
        
        for user in users_data:
            normalized = RandomUserService.normalize_user(user)
            
            serializer = UserSerializer(data=normalized)
            
            serializer.is_valid(raise_exception=True)
            
            serializer.save()
            
            created_users.append(serializer.data)
        
        return Response(
            {
                "message": "Usuarios generados correctamente",
                "total": len(created_users),
                "data": created_users
            }
        )
        