from django.urls import path # Hay un problema con django.cong.urls import urls
# from mysite.settings import MEDIA_ROOT, MEDIA_URL
from . import views


urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="sign up"),
    path('delete/', views.delete_account, name="delete account"),
]
