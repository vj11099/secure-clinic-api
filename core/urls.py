"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from patient_management.views.healthcheck import health_check
from rest_framework import routers
from patient_management.views.patient import PatientViews
from patient_management.views.encounter import EncounterViews
from patient_management.views.user import (
    RegisterUserViews, LoginView, LogoutView)

router = routers.DefaultRouter()

router.register(r'patients', PatientViews, basename='patient-detail')
router.register(r'encounters', EncounterViews, basename='encounter-detail')

urlpatterns = [
    path('auth/register/', RegisterUserViews.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
