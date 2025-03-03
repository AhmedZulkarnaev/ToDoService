# import os
# from celery import Celery
# from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# app = Celery('config')

# app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     """
#     Пример задачи для отладки, которая выводит информацию о запросе задачи.
#     """
#     print(f'Request: {self.request!r}')


# app.conf.beat_schedule = {
#     'check_due_tasks': {
#         'task': 'todo.tasks.check_due_tasks',
#         'schedule': crontab(minute='*/5'),
#     },
# }
