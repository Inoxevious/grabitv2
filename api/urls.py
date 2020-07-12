from django.urls import path
from django.conf.urls import include,url
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import *

urlpatterns = [
    path('users/', UserListView.as_view(), name='users_list'),
    path('users/', UserListCreateView.as_view(), name='users_list'),
    path('user/<uuid:pk>/',  UserDetailView.as_view(), name='user_detail'),
    path('', include(router.urls)),
    url(r'^createpaymentintent/$',createpaymentintent,name='createpaymentintent'),
    path('packages/', PackageListView.as_view(), name='packages_list'),
]