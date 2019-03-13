from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stories', views.StoryView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', views.user_login),
    path('api/logout/', views.user_logout),
    path('api/poststory/', views.post_story),
    path('api/deletestory/', views.delete_story),
    path('api/getstories/', views.get_stories)
]
