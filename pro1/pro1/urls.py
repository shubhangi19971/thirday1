
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import PersonViewSet

router=DefaultRouter()

router.register('person', PersonViewSet, basename='person')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
