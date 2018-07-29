from django.conf.urls import url
from rest_framework import routers
from .views import QuestionViewSet


router = routers.DefaultRouter()
router.register(r'question',QuestionViewSet)

urlpatterns = router.urls
