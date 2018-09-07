
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('events', views.EventView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
