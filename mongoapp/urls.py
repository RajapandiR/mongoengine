from django.urls import path, include
# from django_mongoengine import mongo_admin
from rest_framework import routers

from mongoapp import views

router = routers.DefaultRouter()
router.register('Profile', views.ProfileViewSet, basename='ProfileViewSet')
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('pro/', views.ProfileApiView.as_view()),
    path('pro/<str:pid>', views.ProfileApiView.as_view()),
]