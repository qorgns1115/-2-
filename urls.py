# diary/urls.py
from django.urls import path, include
# diary/urls.py
from rest_framework.routers import DefaultRouter
# from .views import UserProfileViewSet
from .views import DiaryEntryViewSet  # views에서 DiaryEntryViewSet 가져오기
router = DefaultRouter()
# router.register(r'userprofiles', UserProfileViewSet)
router.register(r'diaryentries', DiaryEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

