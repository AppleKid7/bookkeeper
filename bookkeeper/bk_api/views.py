from rest_framework import generics
from serializers import (UserSerializer, PermissionSerializer,
                         GroupSerializer, SignUpSerializer)
from django.contrib.auth.models import User, Permission, Group
from permissions import IsAuthenticatedOrCreate


# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PermissionList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = PermissionSerializer


class PermissionDetail(generics.RetrieveAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)
