from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.mixins import RequestLogMiddleware
from api.services import process_and_request_data
from authentication.serializers import UserCreateSerializer


class UserEndpoint(RequestLogMiddleware, APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response(token.key)
        return Response(serializer.errors, status=400)


class SymbolEndpoint(RequestLogMiddleware, APIView):
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def get(self, request, symbol):
        data = process_and_request_data(symbol)
        if data.get('error'):
            return Response(data, status=400)
        return Response(data)
