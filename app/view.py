from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from app.serializers import UserSerializer
from app.serializers import LinkSerializer
from app.model import Link


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
