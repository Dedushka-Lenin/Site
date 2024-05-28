from django.urls import path, include

from .views import Register

urlpatterns = [
    path('',  include('django.contrib.auth.urls')),

    path('confirm_email/',  Register.as_view(template_name='registration/verify_done.html.html'), name="confirm_email"),
    path("verify/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('register/',  Register.as_view(), name="register"),
]
