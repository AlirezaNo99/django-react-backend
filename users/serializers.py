from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'mobile', 'city', 'province', 'address', 'gender', 'is_premium', 'purchased_products', 'age')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            password=validated_data['password']
        )
        user.is_active = False  # Set inactive until email is verified
        user.save()

        # Send email verification link
        self.send_verification_email(user)

        return user

    def send_verification_email(self, user):
        from django.urls import reverse
        from django.conf import settings
        from rest_framework_simplejwt.tokens import RefreshToken
        from django.core.mail import send_mail

        token = RefreshToken.for_user(user).access_token
        verify_url = f"{settings.FRONTEND_URL}/activate/{str(token)}"
        
        # Send verification email
        send_mail(
            'Verify your email',
            f'Click the link to verify your account: {verify_url}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims (remove 'username' if not needed)
        token['email'] = user.email

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['email'] = self.user.email
        return data