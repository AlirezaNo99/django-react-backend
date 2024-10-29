from rest_framework_simplejwt.views import  TokenRefreshView,TokenVerifyView
from .views import RegisterView, UserView, CustomTokenObtainPairView, UserCount,VerifyEmailView, CustomConfirmEmailView

from django.urls import path,include

urlpatterns = [
path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), 
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
path('users/count/', UserCount.as_view(), name='user-count'),  
path('users/activate/<str:token>/', VerifyEmailView.as_view(), name='email-verify'),
path('auth/registration/account-confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),

path('auth/', include('dj_rest_auth.urls')),  # For login, logout, and password reset
path('auth/registration/', include('dj_rest_auth.registration.urls')),  # For registration and email verification

]