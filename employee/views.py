from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import employee_model
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from .serializers import RegisterSerializer , LoginSerializer , UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class DetailsViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = User.objects.all()
        details_serializer = UserSerializer(data , many = True)
        return Response(details_serializer.data)

class RegisterView(generics.CreateAPIView):

    perimission_class = (AllowAny)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    # if User.objects.filter(username=username).exists(): 
    #     return ({"detail": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST) 

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username , password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            # data = User.objects.all()
            # details_serializer = UserSerializer(data , many = True)
            
            return Response({
                'refresh' : str(refresh),
                'access': str(refresh.access_token),
                'user':user_serializer.data,
                # 'user':details_serializer.data,
            })
        else:
            return Response({'detail': 'invalid credentials'})
        

