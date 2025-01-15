import json
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model, authenticate  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
import jwt
from django.utils import timezone
from datetime import timedelta
from rest_framework_simplejwt.tokens import AccessToken, UntypedToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.authentication import get_authorization_header
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser 
from .serializers import ActiveUserListSerializer
from rest_framework.pagination import PageNumberPagination
from .forms import CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token
from django.http import JsonResponse

User = get_user_model()

def generate_jwt_token(user):
    # Create an access token for the user
    token = AccessToken.for_user(user)
    return str(token)

def send_activation_email(user):
    token = generate_jwt_token(user)
    activation_link = f"{settings.FRONTEND_URL}/activate?token={token}"
    email_subject = "Activate Your Account"
    email_body = f"Click the link to verify your account: {activation_link}"
    send_mail(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, [user.email])

class RegisterView(APIView):
    def post(self, request):
        # Code to create a user, for example, serializer validation and saving
        user = User.objects.create_user(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            username=request.data['username'],
            email=request.data['email'],
            mobile=request.data['mobile'],
            password=request.data['password'],
            is_active=False
        )
        send_activation_email(user)
        return Response({"message": "Activation email sent."}, status=status.HTTP_201_CREATED)

class ActivateAccount(APIView):
    def post(self, request):
        token = request.data.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])
            if not user.is_active:
                user.is_active = True
                user.save()
                return Response({"message": "تبریک! ثبت نام شما تکمیل و حساب کاربری شما فعال شد"}, status=status.HTTP_200_OK)
            return Response({"message": "این حساب کاربری قبلا ثبت و فعال سازی شده است"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.ExpiredSignatureError:
            return Response({"message": "لینک فعال سازی منقضی شده است."}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.InvalidTokenError:
            return Response({"message": "لینک صحیح نمی‌باشد"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "فعال سازی با خطا مواجه شد"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.is_active:
            return Response({"message": "Account is not activated"}, status=status.HTTP_403_FORBIDDEN)
        
        token = generate_jwt_token(user)
        return Response({"token": token}, status=status.HTTP_200_OK)

class StaffLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None or not user.is_staff:
            return Response({"message": "Invalid credentials or not authorized"}, status=status.HTTP_403_FORBIDDEN)
        
        if not user.is_active:
            return Response({"message": "Account is not activated"}, status=status.HTTP_403_FORBIDDEN)
        
        token = generate_jwt_token(user)
        return Response({"token": token}, status=status.HTTP_200_OK)

class VerifyStaffTokenView(APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)

        if not token:
            return Response({"message": "Token is required"}, status=status.HTTP_401_UNAUTHORIZED)

        # Remove "Bearer " prefix if present
        if token.startswith("Bearer "):
            token = token.split(" ")[1]

        try:
            # Validate the token
            UntypedToken(token)  # This will decode the token and raise errors if invalid
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])

            if user.is_staff:
                return Response({"message": "Token is valid", "user_id": user.id,"username":user.username}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Token is valid but user is not staff"}, status=status.HTTP_403_FORBIDDEN)

        except jwt.ExpiredSignatureError:
            return Response({"message": "Token has expired"}, status=status.HTTP_401_UNAUTHORIZED)
        except TokenError:
            return Response({"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

class RetrieveUserInfoAPIView(APIView):
    """
    API endpoint to retrieve user information (first name, last name, and email)
    for non-staff users based on a JWT token.
    """
    def get(self, request):
        # Get the token from the Authorization header
        auth_header = get_authorization_header(request).split()
        
        if not auth_header or auth_header[0].lower() != b"bearer":
            return Response({"error": "Token not provided"}, status=status.HTTP_401_UNAUTHORIZED)

        # Extract token from header
        token = auth_header[1].decode('utf-8')
        
        try:
            # Decode the JWT token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            
            # Fetch the user based on the user ID in the token payload
            user_id = payload.get("user_id")
            user = User.objects.get(id=user_id)
            
            # Check if the user is a non-staff user (as specified in your requirements)
            if user.is_staff:
                return Response({"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN)

            # Return user information
            user_info = {
                "user_id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "mobile":user.mobile
            }
            return Response({"user_info": user_info}, status=status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token has expired"}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

class DeleteUserAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "User account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class EditUserAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        data = request.data

        # Update the user's information with the provided data
        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.email = data.get("email", user.email)
        user.mobile = data.get("mobile", user.mobile)

        user.save()

        return Response({
            "message": "User account updated successfully",
            "user_id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "mobile": user.mobile
        }, status=status.HTTP_200_OK)

class ValidateUserToken(APIView):
    permission_classes = [IsAuthenticated]  # Ensures the token is valid

    def get(self, request):
        user = request.user
        # Check if the user is not staff
        if not user.is_staff:
            return Response({"valid": True, "user": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            }})
        else:
            return Response({"valid": False, "error": "Staff tokens are not allowed."}, status=403)

class ActiveNonStaffUserCountView(APIView):
    def get(self, request):
        count = User.objects.filter(is_active=True, is_staff=False).count()
        return Response({'active_non_staff_count': count}, status=status.HTTP_200_OK)

class CustomPagination(PageNumberPagination):
    page_size = 10  # default page size
    page_size_query_param = 'page_size'
    max_page_size = 100

class ActiveNonStaffUserListView(generics.ListAPIView):
    serializer_class = ActiveUserListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True, is_staff=False)

        # Search by full name (first_name and last_name combined)
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                models.Q(first_name__icontains=search_query) | models.Q(last_name__icontains=search_query)
            )

        # Sort by account activation date or other fields
        sort_by = self.request.query_params.get('sort_by')
        if sort_by:
            sort_fields = sort_by.split(',')
            valid_sort_fields = [field for field in sort_fields if field in ['date_joined', '-date_joined']]
            if valid_sort_fields:
                queryset = queryset.order_by(*valid_sort_fields)

        return queryset

class CustomPasswordResetView(PasswordResetView):
    permission_classes = [AllowAny]

    def dispatch(self, request, *args, **kwargs):
        print(f"Request method: {request.method}")  # Debug request method
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                email = data.get('email')
            else:
                email = request.POST.get('email')
            print(settings.EMAIL_BACKEND)

            print(f"Email received: {email}")  # Debug: print the email

            if not User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email not found."}, status=400)

            return super().post(request, *args, **kwargs)

        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

    def form_valid(self, form):
        print("entered the form valid")
        email = form.cleaned_data['email']
        token = form.reset_token
        uid = form.uid
        reset_link = self.request.build_absolute_uri(f"/reset/{uid}/{token}/")
        print(f"Password reset link for {email}: {reset_link}")  # This should print in the console
        return super().form_valid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def post(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Decode the user ID
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return JsonResponse({"error": "Invalid user ID."}, status=400)

        # Check the token validity
        if not default_token_generator.check_token(user, token):
            return JsonResponse({"error": "Invalid or expired token."}, status=400)
        
        # Validate and set the new password
        if new_password != confirm_password:
            return JsonResponse({"error": "Passwords do not match."}, status=400)
        
        user.set_password(new_password)
        user.save()
        
        return JsonResponse({"success": "Password has been reset successfully."})

def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})