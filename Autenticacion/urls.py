from django.urls import path # Hay un problema con django.cong.urls import urls
# from mysite.settings import MEDIA_ROOT, MEDIA_URL
from Autenticacion import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('logou/', views.logout, name="logout"),
    path('register/', views.signup, name="register"),
    path("forgotPassword/", views.forgotPassword, name="forgot"),
    path("resetPassword/<token>/", views.resetPassword, name="reset"),
    path("updateMyPassword/", views.updatePassword, name="update"),
]