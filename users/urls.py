# users/urls.py
from django.urls import path
from . import views
from .views import RegisterView, ActivateAccount,LoginView,StaffLoginView,RetrieveUserInfoAPIView,DeleteUserAccountView,EditUserAccountView,ValidateUserToken,VerifyStaffTokenView,ActiveNonStaffUserCountView, ActiveNonStaffUserListView, CustomPasswordResetView, CustomPasswordResetConfirmView
urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/activate/', ActivateAccount.as_view(), name='activate-account'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/staff/login/', StaffLoginView.as_view(), name='staff-login'),  
    path('auth/user-info/', RetrieveUserInfoAPIView.as_view(), name='user_info'),
    path('auth/user/edit/', EditUserAccountView.as_view(), name='edit_user_account'),
    path('auth/user/delete/', DeleteUserAccountView.as_view(), name='delete_user_account'),
    path('auth/user/validate-token/', ValidateUserToken.as_view(), name='validate-token'),
    path('auth/staff/verify-token/', VerifyStaffTokenView.as_view(), name='validate-staff-token'),
    path('auth/users/active-non-staff/count/', ActiveNonStaffUserCountView.as_view(), name='active_non_staff_user_count'),
    path('auth/users/active-non-staff/', ActiveNonStaffUserListView.as_view(), name='active_non_staff_user_list'),
    path('auth/users/password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('auth/users/password-reset-confirm/<uidb64>/<token>/',CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'
    ),
    path('csrf-token/', views.csrf_token_view, name='csrf_token'),
]
