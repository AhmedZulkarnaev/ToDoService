from rest_framework import viewsets, permissions
from todo.models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class IsOwner(permissions.BasePermission):
    """
    Проверка, что пользователь является владельцем объекта.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).prefetch_related('categories')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
