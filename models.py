from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    appearance_settings = models.TextField()  # JSON 형식으로 외형 저장
    preferred_art_style = models.CharField(max_length=50, default="crayon")  # 선호하는 그림체

    def __str__(self):
        return self.user.username

class DiaryEntry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text_content = models.TextField()  # 일기 내용
    generated_image_path = models.CharField(max_length=255, blank=True, null=True)  # 이미지 경로

    def __str__(self):
        return f"{self.user.user.username} - {self.date}"
