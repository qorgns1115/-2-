"""
URL configuration for diary_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# from diary import views
# from diary.views import UserProfileViewSet, DiaryEntryViewSet

# router = DefaultRouter()
# router.register(r'userprofiles', UserProfileViewSet)
# router.register(r'diaryentries', DiaryEntryViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('diary.urls')),  # API 엔드포인트
    
# ]
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Diary App API. Go to /api/ for API endpoints.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('diary.urls')),
    path('', home),  # 루트 URL을 home 뷰에 연결
]

