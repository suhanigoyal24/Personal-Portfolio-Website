from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField

class CustomUser(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profiles/',
        default='profiles/default.png',
        blank=True
    )
    job_title = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username


class Portfolio(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    skills = JSONField(default=list, blank=True)
    experience = JSONField(default=list, blank=True)
    template = models.CharField(max_length=50, default='minimal')

    def __str__(self):
        return f"{self.user.username}'s Portfolio"


class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
