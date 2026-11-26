"""
URL configuration for exam_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import FacultySignUpView,FacultyProfileRetrieveUpdateView

from assessment_management.views import AssessmentListCreateView,AssessmentRetrieveUpdateDeleteView

from question_management.views import QuestionCreateView,QuestionRetrieveUpdateDeleteView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),

    #accounts
    path('faculty/signup/',FacultySignUpView.as_view()),
    path('token/',ObtainAuthToken.as_view()),
    path('faculty/profile/',FacultyProfileRetrieveUpdateView.as_view()),

    #assessments
    path('assessments/',AssessmentListCreateView.as_view()),
    path('assessments/<int:pk>/',AssessmentRetrieveUpdateDeleteView.as_view()),

    #questions
    path('assessment/<int:pk>/questions/',QuestionCreateView.as_view()),
    path('question/<int:pk>/',QuestionRetrieveUpdateDeleteView.as_view()),


]
