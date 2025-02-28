# Generated by Django 4.2 on 2025-02-28 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import todo.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(default=todo.utils.generate_unique_id, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(default=todo.utils.generate_unique_id, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Due Date')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('categories', models.ManyToManyField(related_name='task_categories', to='todo.category', verbose_name='Categories')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_category', to='todo.category', verbose_name='Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['due_date', 'created_at'],
            },
        ),
    ]
