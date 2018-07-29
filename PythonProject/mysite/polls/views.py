from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializers import QuestionSerialiser, QuestionBankSerializer
from .models import Question, QuestionBank

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialiser
# Create QuestionBank viewsets
class QuestionBankViewSet(viewsets.ModelViewSet):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer
