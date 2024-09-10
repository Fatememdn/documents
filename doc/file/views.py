from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import PermissionDenied
from .models import TextFile
from .serializers import TextFileCreateUpdateSerializer, TextFileDetailSerializer
from django.http import FileResponse

class UploadFileView(CreateAPIView):
    queryset = TextFile.objects.all()
    serializer_class = TextFileCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EditFileView(UpdateAPIView):
    queryset = TextFile.objects.all()
    serializer_class = TextFileCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.owner != self.request.user:
            raise PermissionDenied("You do not have permission to edit this file.")
        return obj

class DeleteFileView(DestroyAPIView):
    queryset = TextFile.objects.all()
    serializer_class = TextFileDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.owner != self.request.user:
            raise PermissionDenied("You do not have permission to delete this file.")
        return obj

class ListFileView(ListAPIView):
    serializer_class = TextFileDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TextFile.objects.filter(owner=self.request.user)

class RetrieveFileView(RetrieveAPIView):
    queryset = TextFile.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            raise PermissionDenied("You do not have permission to download this file.")
        return FileResponse(obj.file, as_attachment=True, filename=obj.file.name)