from rest_framework import serializers

from accounts.models import User,FacultyProfile

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","password","phone","role"]
        read_only_fields = ["id","role"]
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data,role="faculty")
    
    
class FacultyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=FacultyProfile
        fields="__all__"
        read_only_fields=["id","user","created_at","updated_at"]