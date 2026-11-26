from django.shortcuts import render,get_object_or_404

from assessment_management.models import Assessment
from assessment_management.serializers import AssessmentSerializer

from accounts.permissions import IsOwner


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from datetime import datetime,timedelta

# Create your views here.

class AssessmentListCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
        qs = Assessment.objects.filter(faculty=request.user)
        serializer_instance = AssessmentSerializer(qs,many=True)
        return Response(serializer_instance.data)
        
    def post(self,request):
        form_data = request.data
        
        serializer_instance = AssessmentSerializer(data=form_data)
        
        if serializer_instance.is_valid():
            exam_date = serializer_instance.validated_data.get("exam_date")
            start_time = serializer_instance.validated_data.get("start_time")
            duration = serializer_instance.validated_data.get("duration")
            
            end_date_time = datetime.combine(exam_date,start_time)+timedelta(hours=duration)
            
            end_time = end_date_time.time()
            
            
            serializer_instance.save(faculty=request.user,end_time=end_time)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
    
class AssessmentRetrieveUpdateDeleteView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]
    
    def get(self,request,pk=None):
        qs = get_object_or_404(Assessment,id=pk)
        self.check_object_permissions(request,qs)
        serializer_instance = AssessmentSerializer(qs)
        return Response(serializer_instance.data)
    
    def put(self,request,pk=None):
        form_data = request.data
        instance = get_object_or_404(Assessment,id=pk)
        self.check_object_permissions(request,instance)
        serializer_instance = AssessmentSerializer(data=form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
        
    def delete(self,request,pk=None):
        instance = get_object_or_404(Assessment,id=pk)
        self.check_object_permissions(request,instance)
        instance.delete()
        return Response({"message":"deleted..."})
            