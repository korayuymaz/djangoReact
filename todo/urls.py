from todo.views import ToDoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ToDoViewSet, basename='todo')
urlpatterns = router.urls
