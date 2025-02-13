from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):  # Ensure the model name is ChatMessage
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}..."
