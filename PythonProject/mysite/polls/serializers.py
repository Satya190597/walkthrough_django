from rest_framework import serializers
from .models import Question, QuestionBank

class QuestionSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

# Question Bank serializer
class QuestionBankSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionBank
        fields = '__all__'
