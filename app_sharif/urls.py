from django.urls import path
from app_sharif import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('login/' , views.login_),
    path('logout/', views.logout_),
    path('signup/', views.signup),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
