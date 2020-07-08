from django.db import models
from django.core.files import File
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from backoffice.UserManager import UserManager
from django.contrib.auth.hashers import get_hasher, identify_hasher
import uuid
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True,db_index=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    facebookId = models.CharField(max_length=100, null=True, blank=True,db_index=True)
    android = models.BooleanField(blank=True, default=False)
    ios = models.NullBooleanField(blank=True, default=False, null=True)
    acceptPush = models.BooleanField(default=False)
    pushToken = models.CharField(max_length=100, null=True, blank=True,db_index=True)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('staff'), default=False)
    valid = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = ('User')
        verbose_name_plural = ('Users')
class Package(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reference = models.CharField(max_length=100,db_index=True)
    qrCode = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    picture = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    available = models.BooleanField(default=True)
    valid = models.BooleanField(default=True)
    class Meta:
        verbose_name = ('Package')
        verbose_name_plural = ('Packages')