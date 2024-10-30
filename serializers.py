from rest_framework import serializers
from .models import UserProfile, DiaryEntry

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'appearance_settings', 'preferred_art_style']

class DiaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = ['user', 'date', 'text_content', 'generated_image_path']
