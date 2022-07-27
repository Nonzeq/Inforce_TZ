from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .models import Employee

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    
    
    
class RegisterView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    
