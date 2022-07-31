from django.urls import path

from api.views import UserEndpoint, SymbolEndpoint

urlpatterns = [
    path("register/", UserEndpoint.as_view(), name="register"),
    path("symbol/<str:symbol>/", SymbolEndpoint.as_view(), name="symbol"),
]
