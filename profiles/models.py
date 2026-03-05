from django.conf import settings
from django.db import models
import json

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_img = models.ImageField(upload_to='profiles/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(default='[]', blank=True)      # JSON stored as text
    experience = models.TextField(default='[]', blank=True)  # JSON stored as text

    def get_skills(self):
        return json.loads(self.skills)

    def set_skills(self, skill_list):
        self.skills = json.dumps(skill_list)

    def get_experience(self):
        return json.loads(self.experience)

    def set_experience(self, exp_list):
        self.experience = json.dumps(exp_list)

    def __str__(self):
        return self.user.username
