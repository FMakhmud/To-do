from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser


class TODO(models.Model):
    class TodoStatus(models.TextChoices):
        NEW = "new", "yangi"
        COMPLETED = "completed", 'yakunlangan'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=False)
    memo = models.TextField(null=True)
    is_important = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=TodoStatus.choices, default=TodoStatus.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'





