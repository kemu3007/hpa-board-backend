from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Team, News
from .serializers import TeamSerializer, NewsSerializer


class isLoggedIn(APIView):
    def get(self, request):
        team = TeamSerializer(request.team)
        return Response(team.data, status=status.HTTP_200_OK)


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.filter(is_active=True)


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.filter(is_active=True)