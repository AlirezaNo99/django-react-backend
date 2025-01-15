from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password','mobile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            mobile=validated_data.get('mobile', '')
        )
        self.send_verification_email(user)
        return user

    def send_verification_email(self, user):
        token = RefreshToken.for_user(user).access_token
        verify_url = f"{settings.FRONTEND_URL}/activate/{str(token)}"
        
        send_mail(
            'Verify your email',
            f'Click the link to verify your account: {verify_url}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )
class ActiveUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'mobile']  