from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import RegisterUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class Register(CreateAPIView):
    serializer_class=RegisterUser
    permission_classes=[AllowAny]

class Logout(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"detail": "Logout successful"},
            )
        except Exception:
            return Response(
                {"detail": "Invalid token"},
            ) 