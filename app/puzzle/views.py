from rest_framework import viewsets, filters, permissions

from puzzle.models import Word, Category, Group, Puzzle
from puzzle import serializers


class IsOwner(permissions.BasePermission):
    """Custom permission to only allow owner of an object to edit"""

    def has_permission(self, request, view):
        return request.user.is_authenticated or request.method == "GET"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.method == "GET"


class WordViewSet(viewsets.ModelViewSet):
    """Manage words in the database"""
    search_fields = ["word"]
    filter_backends = (filters.SearchFilter,)
    queryset = Word.objects.all()
    serializer_class = serializers.WordSerializer
    http_method_names = ["get", "post"]


class CategoryViewSet(viewsets.ModelViewSet):
    """Manage categories in the database"""
    search_fields = ["category"]
    filter_backends = (filters.SearchFilter,)
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    http_method_names = ["get", "post"]


class GroupViewSet(viewsets.ModelViewSet):
    """Manage groups in the database"""
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsOwner, ]

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == "retrieve":
            return serializers.GroupDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PuzzleViewSet(viewsets.ModelViewSet):
    """Manage puzzles in the database"""
    queryset = Puzzle.objects.all()
    serializer_class = serializers.PuzzleSerializer
    permission_classes = [IsOwner, ]

    def get_queryset(self):
        queryset = Puzzle.objects.all()
        user = self.request.query_params.get("user")
        if user is not None:
            queryset = Puzzle.objects.filter(user=user)
        return queryset

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == "retrieve":
            return serializers.PuzzleDetailSerialzer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
