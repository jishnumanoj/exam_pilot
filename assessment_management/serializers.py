from rest_framework import serializers

from assessment_management.models import Assessment

from question_management.models import Question
from question_management.serializers import QuestionSerializer

from datetime import datetime

class AssessmentSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField(read_only=True)
    
    questions = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Assessment
        fields = "__all__"
        read_only_fields = ["id","slug","end_time","faculty","created_at","updated_at"]
        
    def get_question_count(self,obj):
        return Question.objects.filter(assessment = obj).count()
    
    def get_questions(self,obj):
        qs = Question.objects.filter(assessment = obj)
        serializer_instance = QuestionSerializer(qs,many=True)
        return serializer_instance.data
        
    def validate(self,validated_data):
        exam_date = validated_data.get("exam_date")
        if exam_date < datetime.today().date():
            raise serializers.ValidationError("invalid date")
        
        
        return validated_data