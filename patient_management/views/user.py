from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions, status
from ..serializers.user import (RegisterSerializer,
                                CustomTokenObtainPairSerializer)
from ..models.user import User


class RegisterUserViews(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Registration successful! Please check your email to verify your account",
            "token": refresh,
            "email": user.email
        }, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")

            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            return Response({
                "message": "Logout successful"
            }, status=status.HTTP_200_OK)

        except Exception:
            return Response({
                "error": "Invalid token or already logged out"
            }, status=status.HTTP_400_BAD_REQUEST)
