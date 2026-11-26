from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from accounts.serializers import FacultySerializer,FacultyProfileSerializer
from accounts.models import FacultyProfile

# Create your views here.

class FacultySignUpView(CreateAPIView):
    
    serializer_class=FacultySerializer
    
    
class FacultyProfileRetrieveUpdateView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
        auth_user = request.user
        qs=FacultyProfile.objects.get(user=auth_user)
        #qs=auth_user.faculty_profile
        serializer_instance = FacultyProfileSerializer(qs)
        return Response(serializer_instance.data)
    
    def put(self,request):
        form_data = request.data
        instance=FacultyProfile.objects.get(user=request.user)
        serializer_instance = FacultyProfileSerializer(data=form_data,instance=instance)
        
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)