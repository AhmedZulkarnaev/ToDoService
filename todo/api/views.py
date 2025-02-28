from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from todo.models import Task, Category
from todo.api.serializers import TaskSerializer, CategorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Task.
    """
    queryset = Task.objects.all().order_by('category__name')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Category.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
