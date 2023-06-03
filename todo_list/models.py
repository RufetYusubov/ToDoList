from django.db import models
from django.contrib.auth.models import User

class ToDoListModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_todolist")
    name = models.CharField(max_length=300)
    starttime = models.TimeField(blank=True,null=True)
    endtime = models.TimeField(blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "todolist"

    def __str__(self):
        return self.user.username
