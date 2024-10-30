# diary/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DiaryEntry

@receiver(post_save, sender=DiaryEntry)
def generate_image(sender, instance, created, **kwargs):
    if created:
        # 외부 API 호출하여 이미지 생성 및 경로 저장
        instance.generated_image_path = 'path/to/generated_image.png'
        instance.save()
