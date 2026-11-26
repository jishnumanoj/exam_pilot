from rest_framework import serializers

from question_management.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = "__all__"
        read_only_fields = ["id","slug","assessment","order","created_at","updated_at"]
        
    