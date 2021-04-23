from django.urls import path, include
from rest_framework.routers import DefaultRouter

from puzzle import views

router = DefaultRouter()
router.register("words", views.WordViewSet)
router.register("categories", views.CategoryViewSet)
router.register("groups", views.GroupViewSet)
router.register("puzzles", views.PuzzleViewSet)

app_name = "puzzle"

urlpatterns = [
    path("", include(router.urls))
]
