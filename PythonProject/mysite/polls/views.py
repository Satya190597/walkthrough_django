from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializers import QuestionSerialiser
from .models import Question

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialiser
