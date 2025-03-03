from rest_framework import serializers
from todo.models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'created_at', 'deadline', 'categories', 'category_ids']
        read_only_fields = ['user', 'created_at']

    def create(self, validated_data):
        category_ids = validated_data.pop('category_ids', [])
        task = Task.objects.create(**validated_data)
        if category_ids:
            categories = Category.objects.filter(id__in=category_ids)
            task.categories.set(categories)
        return task

    def update(self, instance, validated_data):
        category_ids = validated_data.pop('category_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if category_ids is not None:
            categories = Category.objects.filter(id__in=category_ids)
            instance.categories.set(categories)
        return instance
