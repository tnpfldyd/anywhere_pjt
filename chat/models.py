from django.db import models
from django.conf import settings

# Create your models here.


class MessageRoom(models.Model):
    touser = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="senduser"
    )
    fromuser = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiveruser"
    )
    count = models.IntegerField(default=0)
    last_user = models.CharField(max_length=50)
    last_message = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


class DirectMessage(models.Model):
    room_number = models.ForeignKey(MessageRoom, on_delete=models.CASCADE)
    who = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="who")
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
