from rest_framework import serializers

from todo.models import Task, Category


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Task.

    Сериализует все поля модели Task для использования в API.
    """

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'created_at', 'due_date',
            'completed', 'category', 'user'
        ]


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category.
    """
    class Meta:
        model = Category
        fields = ['id', 'name']
