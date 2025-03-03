# from celery import shared_task
# from django.core.mail import send_mail, BadHeaderError
# from django.utils import timezone

# from todo.models import Task


# @shared_task
# def send_task_notification(task_id):
#     """
#     Отправляет уведомление по электронной почте пользователю о наступлении
#     даты исполнения задачи.

#     Аргументы:
#     task_id (str): Идентификатор задачи.

#     Исключения:
#     Task.DoesNotExist: Если задача с указанным идентификатором не существует.
#     """
#     try:
#         task = Task.objects.get(id=task_id)
#         if task.due_date is not None and task.due_date <= timezone.now():
#             try:
#                 send_mail(
#                     'Task Due Notification',
#                     f'The task "{task.title}" is due.',
#                     'from@example.com',
#                     [task.user.email],
#                     fail_silently=False,
#                 )
#             except BadHeaderError:
#                 print(
#                     f"Invalid header found when sending email to "
#                     f"{task.user.email}"
#                 )
#             except Exception as e:
#                 print(f"Error sending email to {task.user.email}: {e}")
#     except Task.DoesNotExist:
#         pass


# @shared_task
# def check_due_tasks():
#     """
#     Проверяет задачи с наступающей датой исполнения и отправляет
#     уведомления пользователям.

#     Эта задача выполняется периодически и проверяет все задачи, у которых
#     дата исполнения меньше или равна текущему времени и которые еще не
#     завершены. Для каждой такой задачи
#     вызывается задача send_task_notification для отправки уведомления.
#     """
#     now = timezone.now()
#     due_tasks = Task.objects.filter(due_date__lte=now, completed=False)
#     for task in due_tasks:
#         send_task_notification.delay(task.id)