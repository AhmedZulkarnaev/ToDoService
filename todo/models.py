from django.db import models
from django.contrib.auth.models import User

from todo.utils import generate_unique_id


class Task(models.Model):
    """
    Модель задачи (Task), представляющая задачу в системе.
    """
    id = models.CharField(
        max_length=20,
        primary_key=True,
        default=generate_unique_id,
        editable=False
    )
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    due_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Due Date"
    )
    completed = models.BooleanField(default=False, verbose_name="Completed")
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name="Category",
        related_name="task_category"
    )
    categories = models.ManyToManyField(
        'Category',
        verbose_name="Categories",
        related_name="task_categories"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="tasks"
    )

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['due_date', 'created_at']

    def __str__(self) -> str:
        status = "Completed" if self.completed else "Pending"
        return f'{self.title} - {self.category.name} - {status}'


class Category(models.Model):
    """
    Модель категории (Category), представляющая категорию задач.
    """
    id = models.CharField(
        max_length=20,
        primary_key=True,
        default=generate_unique_id,
        editable=False
    )
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
