from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.services import process_and_request_data
from authentication.serializers import UserCreateSerializer


class UserEndpoint(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)

            return Response(token.key)
        return Response(serializer.errors)


class SymbolEndpoint(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def get(self, request, symbol):
        data = process_and_request_data(symbol)
        return Response(data)
