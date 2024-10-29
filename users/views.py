from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from allauth.account.views import ConfirmEmailView
from django.core.exceptions import ValidationError  
from allauth.account.models import EmailAddress
from django.conf import settings
User = get_user_model()

from django.http import HttpResponseRedirect
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = User.objects.get(id=user_id)

            if not user.is_active:
                user.is_active = True
                user.save()
                return HttpResponseRedirect(f'{settings.FRONTEND_URL}/verifyAccount?status=success')
            return HttpResponseRedirect(f'{settings.FRONTEND_URL}/verifyAccount?status=already_active')
        except Exception as e:
            logger.error(f"Error during account activation: {e}")
            return HttpResponseRedirect(f'{settings.FRONTEND_URL}/verifyAccount?status=failed')

class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            
            email_address = EmailAddress.objects.filter(
                email=self.object.email_address.email,  
                user=self.object.email_address.user,    
                verified=True                           
            ).first()  
            
            if email_address:
                return HttpResponseRedirect(f'{settings.FRONTEND_URL}/verifyAccount?status=success')
            else:
                return HttpResponseRedirect(f'{settings.FRONTEND_URL}/verifyAccount?status=failed')
        except ValidationError:
            return HttpResponseRedirect(f'{settings.FRONTEND_URL}/verifyAccount?status=failed')


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserCount(APIView):

    def get(self, request):
        total_users = User.objects.count()
        return Response({"total_users": total_users})
