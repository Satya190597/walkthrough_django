from django.conf.urls import url
from rest_framework import routers
from .views import QuestionViewSet, QuestionBankViewSet


router = routers.DefaultRouter()
router.register(r'question',QuestionViewSet)
router.register(r'questionbank',QuestionBankViewSet)

urlpatterns = router.urls
