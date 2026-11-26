from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=15)
    ROLE_CHOICES = (
        ("faculty","Faculty"),
        ("student","Student")
    )
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default="student")
    
class FacultyProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="faculty_profile")
    bio = models.TextField(blank=True,null=True)
    department = models.CharField(max_length=200,blank=True)
    designation = models.CharField(max_length=100,blank=True)
    qualification = models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"FacultyProfile: {self.user.username}"

class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student_profile")
    bio = models.TextField(blank=True,null=True)
    department = models.CharField(max_length=200,blank=True)
    course = models.CharField(max_length=200,blank=True)
    enrollment_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"StudentProfile: {self.user.username}"
    
# signals

def create_faculty_profile(sender,instance,created,**kwargs):
    if created and instance.role == "faculty":
        FacultyProfile.objects.create(user=instance)
        
def create_student_profile(sender,instance,created,**kwargs):
    if created and instance.role == "student":
        FacultyProfile.objects.create(user=instance)
        
post_save.connect(create_faculty_profile,sender=User)

post_save.connect(create_student_profile,sender=User)
    