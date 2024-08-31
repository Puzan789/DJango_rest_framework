from .models import Student
from rest_framework.generics import GenericAPIView
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.throttling import Jackcreatethrottle

class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]   
    # throttle_classes=[Jackcreatethrottle, AnonRateThrottle]  # throttle based on user and anon requests
    throttle_classes=[Jackcreatethrottle, AnonRateThrottle]  # throttle based on user and anon requests

  