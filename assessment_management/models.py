from django.db import models

from django.utils.text import slugify

# Create your models here.

from accounts.models import User

class Assessment(models.Model):
    
    title = models.CharField(max_length=200)
    
    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )
    
    batch = models.CharField(max_length=200)
    
    exam_date = models.DateField()
    
    duration = models.PositiveIntegerField()
    
    start_time = models.TimeField()
    
    end_time = models.TimeField(null=True)
    
    faculty = models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_assessments")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]