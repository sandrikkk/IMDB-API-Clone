from rest_framework.decorators import api_view
from . serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app import models
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'],)
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status = 200)

@api_view(['POST'],)
def Registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        print(data)
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            
            # token = Token.objects.get(user = account).key
            # data['token'] = token
            refresh = RefreshToken.for_user(account)
            data['token'] ={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

        else:
            data = serializer.errors    
            
        return Response(data)