from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class SongView(ListCreateAPIView, PageNumberPagination):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        found_album = get_object_or_404(Album, pk=self.kwargs.get("pk"))
        return serializer.save(album=found_album)

