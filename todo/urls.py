from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

router = DefaultRouter()
router.register('api/todo', views.TODOViewSet, basename="todo")

urlpatterns = router.urls
urlpatterns += [
    path('register/', views.RegisterAPI.as_view()),
    path('login/', views.LoginAPI.as_view()),
]
