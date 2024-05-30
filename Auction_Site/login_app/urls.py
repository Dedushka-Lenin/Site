from django.urls import path, include

from .views import Register, EmailVerify

urlpatterns = [
    path('',  include('django.contrib.auth.urls')),

    path('confirm_email/',  Register.as_view(template_name='registration/verify_done.html.html'), name="confirm_email"),
    path("verify/<uidb64>/<token>/", EmailVerify.as_view(), name="verify_email.html"),

    path('register/',  Register.as_view(), name="register"),
]
